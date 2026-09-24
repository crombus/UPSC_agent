from __future__ import annotations
import json, os, re, shutil, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent
VALIDATOR=ROOT/'validate_package.py'
CASES=[
 ('missing-required','delete','README.md','MISSING_REQUIRED_FILE'),
 ('missing-markdown-stale-success','delete','MCQ-QUESTIONS.md','MISSING_REQUIRED_FILE'),
 ('destination-tamper','replace','FORMAL-SOURCE-MIRROR.md','DESTINATION_PAYLOAD_HASH_MISMATCH'),
 ('source-hash-tamper','source_hash','FORMAL-COVERAGE-REVIEW.json','SOURCE_HASH_MISMATCH'),
 ('semantic-excerpt','semantic','FORMAL-COVERAGE-REVIEW.json','SEMANTIC_PROPOSITION_QUALITY'),
 ('child-union','child','FORMAL-COVERAGE-REVIEW.json','CHILD_UNION_MISMATCH'),
 ('segment-hash','segment','FORMAL-COVERAGE-REVIEW.json','LARGE_LEAF_SEGMENT_HASH'),
 ('missing-cell','missing_cell','TEST-MATRIX.json','TEST_MATRIX_CELL_COUNT'),
 ('false-mapping','false_mapping','TEST-MATRIX.json','MCQ_FALSE_MAPPING'),
 ('overloaded-mapping','overload','TEST-MATRIX.json','MCQ_OVERLOADED_MAPPING'),
 ('redundant-mapping','redundant','TEST-MATRIX.json','MCQ_REDUNDANT_MAPPING'),
 ('distractor-only-evidence','distractor_evidence','MCQ-SOLUTIONS.md','MCQ_PRIMARY_EVIDENCE_MISSING'),
 ('legacy-fixed-count','legacy','README.md','LEGACY_FIXED_COUNT_CONTRACT'),
 ('severe-imbalance','answers','MCQ-SOLUTIONS.md','MCQ_POSITION_IMBALANCE'),
 ('predictable-cycle','cycle','MCQ-SOLUTIONS.md','MCQ_PREDICTABLE_CYCLE'),
 ('duplicate-question-id','duplicate_q','MCQ-SOLUTIONS.md','MCQ_DUPLICATE_ID'),
 ('noncontiguous-questions','noncontiguous','MCQ-QUESTIONS.md','MCQ_NONCONTIGUOUS_NUMBERING'),
 ('mismatched-options','option','MCQ-SOLUTIONS.md','MCQ_SOLUTION_OPTIONS_MISMATCH'),
 ('missing-answer','missing_answer','MCQ-SOLUTIONS.md','MCQ_ANSWER_MISSING'),
 ('stale-markdown-source','bank_stale','MCQ-BANK.json','MCQ_AUDIT_STALE'),
 ('matrix-audit-stale','matrix_stale','TEST-MATRIX.json','MCQ_AUDIT_STALE'),
 ('option-length-cue','length_cue','MCQ-SOLUTIONS.md','MCQ_OPTION_LENGTH_CUE'),
 ('noncompetitive-distractor','categorical_filler','MCQ-SOLUTIONS.md','MCQ_NONCOMPETITIVE_DISTRACTOR'),
]
def invoke(copy,release=False):
 cmd=[sys.executable,'-B',str(copy/'validate_package.py'),'--root',str(copy),'--check-only']+(['--release'] if release else [])
 env=dict(os.environ); env['PYTHONDONTWRITEBYTECODE']='1'
 p=subprocess.run(cmd,text=True,capture_output=True,env=env)
 try:data=json.loads(p.stdout)
 except Exception:data={'errors':[{'code':'UNPARSEABLE','detail':p.stdout+p.stderr}]}
 return p.returncode,data
def prepare(copy):
 shutil.copytree(ROOT,copy,ignore=shutil.ignore_patterns('.negative-tests-work','__pycache__','*.pyc','generate_mcq_bank.py'))
def git_run(copy,*args,check=True):
 return subprocess.run(['git','-C',str(copy),*args],check=check,text=True,capture_output=True)
def prepare_git_repo(copy,omit=()):
 prepare(copy)
 omitted={}
 for rel in omit:
  path=copy/rel; omitted[rel]=path.read_bytes(); path.unlink()
 git_run(copy,'init','--quiet')
 git_run(copy,'config','user.email','jainism-validator@example.invalid')
 git_run(copy,'config','user.name','Jainism Validator Test')
 git_run(copy,'add','--all')
 git_run(copy,'commit','--quiet','-m','baseline')
 for rel,data in omitted.items():
  path=copy/rel; path.parent.mkdir(parents=True,exist_ok=True); path.write_bytes(data)
def replace_rendered_option(text,number,letter,replacement):
 pattern=rf'(^## MCQ {number}\..*?^){letter}\.\s+(.+?)(?=\n\n[A-D]\.\s+|\n\n\*\*Answer:|\n<a id=|\n## |\Z)'
 return re.sub(pattern,lambda m:m.group(1)+f'{letter}. {replacement}',text,count=1,flags=re.M|re.S)
def mutate(copy,kind,rel):
 p=copy/rel
 if kind=='delete': p.unlink(); return
 text=p.read_text(encoding='utf-8')
 if kind=='replace':
  review=json.loads((copy/'FORMAL-COVERAGE-REVIEW.json').read_text(encoding='utf-8')); a=review['decisions'][0]['destination']['anchor']; text=text.replace(f'<a id="{a}"></a>',f'<a id="{a}"></a>\nTAMPER',1)
 elif kind in {'source_hash','semantic','child','segment'}:
  d=json.loads(text)
  if kind=='source_hash': d['sources']['formal_session']['sha256']='0'*64
  elif kind=='semantic': d['decisions'][0]['semantic_propositions']=['Generic excerpt.']
  elif kind=='child': next(x for x in d['decisions'] if x['direct_children'])['child_union_sha256']='0'*64
  else: next(x for x in d['decisions'] if x['large_leaf_segments'])['large_leaf_segments'][0]['payload_sha256']='0'*64
  text=json.dumps(d,ensure_ascii=False,indent=2)+'\n'
 elif kind in {'missing_cell','false_mapping','overload','redundant','matrix_stale'}:
  d=json.loads(text)
  if kind=='missing_cell': d['cells'].pop()
  elif kind=='false_mapping': d['cells'][0]['mapped_question']='Q002'
  elif kind=='overload': d['question_mappings']['Q001']['cell_ids']=['J-001','J-002']
  elif kind=='redundant': d['question_mappings']['Q002']['cell_ids']=['J-001']; d['cells'][1]['mapped_question']='Q002'
  else: d['derivation_policy']+=' mutated'
  text=json.dumps(d,ensure_ascii=False,indent=2)+'\n'
 elif kind=='distractor_evidence':
  matrix=json.loads((copy/'TEST-MATRIX.json').read_text(encoding='utf-8')); a=matrix['cells'][0]['semantic_assertions'][0]
  text=text.replace('Correct: '+a,'Correct: The keyed explanation was stripped of its discriminator.',1)
  text=text.replace('- **A:** Incorrect:',f'- **A:** Incorrect: {a} ',1)
 elif kind=='legacy': text+='\nExact 32 questions are sufficient for this package.\n'
 elif kind in {'answers','cycle'}:
  seq='A'*94 if kind=='answers' else ('ABCD'*24)[:94]; it=iter(seq)
  text=re.sub(r'\*\*Answer:\s*[A-D]\.\*\*',lambda _:f'**Answer: {next(it)}.**',text)
  ap=copy/'MCQ-AUDIT.json'; a=json.loads(ap.read_text(encoding='utf-8')); a['answer_sequence']=seq; a['answer_counts']={x:seq.count(x) for x in 'ABCD'}; a['position_policy']['predictable_cycle_detected']=kind=='cycle'; ap.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
 elif kind=='duplicate_q': text=text.replace('## MCQ 94.','## MCQ 93.',1)
 elif kind=='noncontiguous': text=text.replace('## MCQ 94.','## MCQ 95.',1)
 elif kind=='option': text=text.replace('A. ','A. Mutated option: ',1)
 elif kind=='missing_answer': text=re.sub(r'\*\*Answer:\s*[A-D]\.\*\*','**Answer: E.**',text,count=1)
 elif kind=='bank_stale':
  d=json.loads(text); d['questions'][0]['title']+=' stale'; text=json.dumps(d,ensure_ascii=False,indent=2)+'\n'
 elif kind in {'length_cue','categorical_filler'}:
  answer=re.search(r'^## MCQ 1\..*?\*\*Answer:\s*([A-D])\.\*\*',text,re.M|re.S).group(1)
  distractors=[letter for letter in 'ABCD' if letter!=answer]
  replacements=(
   ['Ten prophets constitute the lineage.','Mahavira alone founded the religion.','Every siddha was once tirthankara.']
   if kind=='length_cue' else
   ['None of the above.']
  )
  targets=distractors if kind=='length_cue' else distractors[:1]
  for target,replacement in zip(targets,replacements):
   text=replace_rendered_option(text,1,target,replacement)
  question_path=copy/'MCQ-QUESTIONS.md'
  question_text=question_path.read_text(encoding='utf-8')
  for target,replacement in zip(targets,replacements):
   question_text=replace_rendered_option(question_text,1,target,replacement)
  question_path.write_text(question_text,encoding='utf-8',newline='\n')
 elif kind=='append': text+='\nStale source mutation.\n'
 p.write_text(text,encoding='utf-8',newline='\n')
def main():
 work=ROOT/'.negative-tests-work'; shutil.rmtree(work,ignore_errors=True); work.mkdir(); results=[]
 def record(name,expected,rc,data):
  codes=[e.get('code') for e in data.get('errors',[])]
  results.append({'case':name,'expected':expected,'returncode':rc,'codes':codes,'passed':rc!=0 and expected in codes})
 try:
  for name,kind,rel,expected in CASES:
   copy=work/name; prepare(copy); mutate(copy,kind,rel); rc,data=invoke(copy); record(name,expected,rc,data)

  copy=work/'release-corrective-mixed'
  prepare_git_repo(copy,omit=('MCQ-BANK.json',))
  (copy/'README.md').write_text((copy/'README.md').read_text(encoding='utf-8')+'\n',encoding='utf-8',newline='\n')
  git_run(copy,'add','README.md','MCQ-BANK.json')
  rc,data=invoke(copy,True)
  results.append({
   'case':'release-corrective-mixed','expected':'RELEASE_PASS','returncode':rc,
   'codes':[e.get('code') for e in data.get('errors',[])],
   'passed':rc==0 and data.get('state')=='RELEASE_PASS',
  })

  copy=work/'release-unstaged-modified-required'
  prepare_git_repo(copy)
  (copy/'README.md').write_text((copy/'README.md').read_text(encoding='utf-8')+'\nUnstaged change.\n',encoding='utf-8',newline='\n')
  rc,data=invoke(copy,True); record('release-unstaged-modified-required','GIT_PACKAGE_UNSTAGED',rc,data)

  copy=work/'release-untracked-required'
  prepare_git_repo(copy,omit=('MCQ-BANK.json',))
  rc,data=invoke(copy,True); record('release-untracked-required','GIT_REQUIRED_NOT_TRACKED',rc,data)

  copy=work/'release-staged-content-stale'
  prepare_git_repo(copy)
  readme=copy/'README.md'
  readme.write_text(readme.read_text(encoding='utf-8')+'\nStaged change.\n',encoding='utf-8',newline='\n')
  git_run(copy,'add','README.md')
  readme.write_text(readme.read_text(encoding='utf-8')+'Working-tree change.\n',encoding='utf-8',newline='\n')
  rc,data=invoke(copy,True); record('release-staged-content-stale','GIT_STAGED_CONTENT_STALE',rc,data)

  copy=work/'release-missing-required'
  prepare_git_repo(copy)
  (copy/'README.md').unlink()
  rc,data=invoke(copy,True); record('release-missing-required','MISSING_REQUIRED_FILE',rc,data)
 finally: shutil.rmtree(work,ignore_errors=True)
 out={'total':len(results),'passed':sum(x['passed'] for x in results),'results':results}; print(json.dumps(out,indent=2)); return 0 if all(x['passed'] for x in results) else 1
if __name__=='__main__': raise SystemExit(main())
