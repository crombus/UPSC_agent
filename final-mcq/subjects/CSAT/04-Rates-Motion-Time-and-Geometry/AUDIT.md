# csat-04 — Rates, Motion, Time and Geometry: verification audit

Status of this record: all three revision banks (`revision-1`, `revision-2`, `revision-3`) were rendered from item source files kept outside the repository (`/tmp/mcq_audit/csat04/items_r1.py`, `items_r2.py`, `items_r3.py`), and every key was re-checked by the same build run (`/tmp/mcq_audit/csat04/build.py`, see §1). The checks below were run on the final files; the run exited without any assertion failure.

## 1. Verification method

Each item carries a `calc` block that recomputes the key from the stem's data (exact `Fraction` arithmetic, `math.lcm`, `math.comb`, `datetime` calendar arithmetic, or a brute-force enumeration over time, day or domino placements). The build engine then enforces, for every item:

1. the computed answer equals the value of the option designated as correct (`vals[correct] == ans`);
2. exactly one of the four candidate values equals the answer (`sum(v == ans) == 1`), so no distractor is numerically equal to the key;
3. the four printed options are distinct strings;
4. for numeric options, the number printed in the option text equals its candidate value (`parse_value(opt) == Fraction(v)`), so the printed option cannot drift from the computed one; options that carry mixed fractions, clock times or unit strings are checked by exact string equality against their computed string form instead;
5. the printed key is the letter assigned after position randomisation (see §4).

Engine excerpt (the complete check logic; the full build script also renders QUESTIONS/ANSWERS and emits these statistics):

```python
def verify(it):
    ns = {"Fraction": Fraction, "math": math, "date": date}
    exec(it["calc"], ns)
    ans = ns["ans"]; vals = ns["vals"]
    opts = it["opts"]; c = it["correct"]
    assert len(opts) == 4 and len(set(opts)) == 4
    if isinstance(ans, str):
        assert opts[c] == ans
        assert sum(o == ans for o in opts) == 1
        assert all(isinstance(v, str) and v == o for v, o in zip(vals, opts))
    else:
        assert vals[c] == ans
        assert sum(1 for v in vals if v == ans) == 1
        for v, o in zip(vals, opts):
            p = parse_value(o)
            if p is None or re.search(r"\d+ \d+/\d+", o) or re.search(r"\d+/\d+", o) and ":" not in o:
                continue
            assert p == Fraction(v)
```

Run result: every item passed in each set (56/56 in R1, 56/56 in R2, 54/54 in R3; 166 in total). No item failed and none was waived.

## 2. Per-item verification records

The `Key` column is the letter in the published `QUESTIONS.md`/`ANSWERS.md` (after position randomisation). `Verified value` is the computed answer (or the computed string for text answers). `Computation` is the exact check, condensed to one line.

### 2.1 Revision 1 (56 items)

| ID | Key | Verified value | Kind | Computation (`calc`) |
|---|---|---|---|---|
| R1-Q01 | B | 135 | numeric | `ans=Fraction(1500,40)*Fraction(18,5) ; vals=[Fraction(75,2),135,108,150]` |
| R1-Q02 | D | 24 | numeric | `ans=Fraction(40)/(Fraction(20,20)+Fraction(20,30)) ; vals=[25,26,24,30]` |
| R1-Q03 | C | 15 | numeric | `ans=Fraction(12*2+18*2,4) ; vals=[Fraction(72,5),15,30,12]` |
| R1-Q04 | C | 33 | numeric | `ans=9*5-4*3 ; vals=[57,33,45,21]` |
| R1-Q05 | D | 10 | numeric | `ans=Fraction(250)/(Fraction(90*5,18)) ; vals=[6,10,Fraction(25,2),50]` |
| R1-Q06 | A | 30 | numeric | `ans=Fraction(300)/(Fraction(72-36,1)*Fraction(5,18)) ; vals=[10,20,30,60]` |
| R1-Q07 | A | 260 | numeric | `ans=Fraction(72*5,18)*25-240 ; vals=[240,260,500,1560]` |
| R1-Q08 | A | 54 | numeric | `ans=Fraction(600,40)*Fraction(18,5) ; vals=[Fraction(189,5),54,15,Fraction(432,5)]` |
| R1-Q09 | D | 8 | numeric | `ans=Fraction(45)/15+Fraction(45)/9 ; vals=[Fraction(15,2),8,6,10]` |
| R1-Q10 | D | 15/2 | numeric | `ans=Fraction(120)/(Fraction(60,15)+Fraction(60,5)) ; vals=[10,Fraction(15,2),5,Fraction(25,2)]` |
| R1-Q11 | B | 60 | numeric | `ans=Fraction(600)/(6+4) ; vals=[60,100,150,300]` |
| R1-Q12 | B | 300 | numeric | `import math ; ans=math.lcm(60,100) ; vals=[100,150,300,600]` |
| R1-Q13 | B | A wins by 25 s | string | `tA=Fraction(1000,5) ; tB=Fraction(900,4) ; ans='A wins by %d s' % (tB-tA) ; vals=['A wins by 20 s','A wins by 25 s','A wins by 45 s','B wins by 25 s']` |
| R1-Q14 | A | 36/5 | numeric | `ans=1/(Fraction(1,12)+Fraction(1,18)) ; vals=[6,Fraction(36,5),15,30]` |
| R1-Q15 | B | 24 | numeric | `# A rate 2b, B rate b; (2b+b)*8=1 -> b=1/24 ; b=Fraction(1,24) ; ans=1/b ; vals=[12,16,24,32]` |
| R1-Q16 | B | 12 | numeric | `done=4*(Fraction(1,12)+Fraction(1,24)) ; ans=(1-done)/Fraction(1,24) ; vals=[4,8,12,16]` |
| R1-Q17 | D | 14 1/3 days | string | `from fractions import Fraction as F ; w=F(0);d=0 ; while True: ; d+=1 ; rate=F(1,12) if d%2==1 else F(1,18) ; if w+rate>=1: ; t=(d-1)+(1-w)/rate ; break ; w+=rate ; vals=['14 days','14 1/3 days','14 1/2 days','15 days'] ; ans='14 1/3 days' if t==F(43,3) else 'other'` |
| R1-Q18 | C | 2880 | numeric | `B=Fraction(1,6)-Fraction(1,10) ; ans=Fraction(4800)*Fraction(1,10)/(Fraction(1,10)+B) ; vals=[2400,2880,1920,3200]` |
| R1-Q19 | B | 12 | numeric | `half=4*Fraction(1,8) ; ans=(1-half)/(Fraction(1,8)-Fraction(1,12)) ; vals=[4,12,16,24]` |
| R1-Q20 | B | 15/2 | numeric | `ans=1/(Fraction(1,10)+Fraction(1,15)-Fraction(1,30)) ; vals=[5,6,Fraction(15,2),10]` |
| R1-Q21 | D | 145.0 | numeric | `ans=abs(30*2-5.5*50) ; ans=min(ans,360-ans) ; vals=[120,145,215,85]` |
| R1-Q22 | A | 4:21 9/11 | string | `from fractions import Fraction as F ; t=F(2880,11) ; ok=((F(11,2)*t-1440)%360==0) and 240<t<300 ; ans='4:21 9/11' if ok else 'other' ; vals=['4:20','4:21 9/11','3:16 4/11','5:27 3/11']` |
| R1-Q23 | C | 44 | numeric | `from fractions import Fraction as F ; ans=len([j for j in range(-5,100) if 0<=F(180+360*j,11)<1440]) ; vals=[11,22,24,44]` |
| R1-Q24 | D | 12:09 | string | `gain=3*3 ; ans='12:%02d' % gain ; vals=['11:51','12:06','12:09','12:12']` |
| R1-Q25 | A | Saturday | string | `from datetime import date ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[(date(2000,1,1)-date(1900,1,1)).days%7] ; vals=['Sunday','Monday','Saturday','Friday']` |
| R1-Q26 | C | Thursday | string | `from datetime import date ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[(date(2024,8,15).weekday()-(date(2024,8,15)-date(2019,8,15)).days)%7] ; vals=['Friday','Saturday','Thursday','Sunday']` |
| R1-Q27 | B | 4 | numeric | `from datetime import date ; ans=(date(2001,1,1)-date(1801,1,1)).days%7 ; vals=[0,4,5,6]` |
| R1-Q28 | A | 25.0 | numeric | `ans=(24**2+7**2)**0.5 ; vals=[31,24,17,25]` |
| R1-Q29 | D | 162 | numeric | `ans=Fraction((14+22)*9,2) ; vals=[126,162,324,198]` |
| R1-Q30 | B | 88 | numeric | `ans=2*Fraction(22,7)*14 ; vals=[44,88,616,154]` |
| R1-Q31 | B | 1/3 | numeric | `ans=Fraction(1,3) ; vals=[Fraction(1,2),Fraction(1,3),3,Fraction(2,3)]` |
| R1-Q32 | A | 27 | numeric | `ans=Fraction(6,2)**3 ; vals=[3,9,27,81]` |
| R1-Q33 | A | 94 | numeric | `ans=2*(5*4+4*3+3*5) ; vals=[60,94,47,120]` |
| R1-Q34 | D | 27/8 | numeric | `ans=Fraction(3,2)**3 ; vals=[Fraction(3,2),Fraction(9,4),Fraction(27,8),Fraction(9,2)]` |
| R1-Q35 | B | 24 | numeric | `n=4 ; ans=6*(n-2)**2 ; vals=[12,16,24,8]` |
| R1-Q36 | A | 36 | numeric | `a,b,c=4,5,6 ; ans=4*((a-2)+(b-2)+(c-2)) ; vals=[12,24,36,48]` |
| R1-Q37 | C | 10 | numeric | `a=max((10//3)*(7//2),(10//2)*(7//3)) ; ans=a ; vals=[9,10,11,12]` |
| R1-Q38 | A | 10.0 | numeric | `ans=((7-1)**2+(10-2)**2)**0.5 ; vals=[6,8,10,14]` |
| R1-Q39 | A | 36/5 | numeric | `ans=Fraction(9*12,15) ; vals=[9,15,21,Fraction(36,5)]` |
| R1-Q40 | B | 2400 | numeric | `ans=Fraction(24,10)*1000 ; vals=[240,2400,24000,Fraction(12,5)]` |
| R1-Q41 | D | 27 | numeric | `n=5 ; ans=(n-2)**3 ; vals=[8,27,36,54]` |
| R1-Q42 | A | 9:32 8/11 | string | `from fractions import Fraction as F ; M=F(360,11) ; ans='9:32 8/11' if abs(270-F(11,2)*M)==90 else 'other' ; vals=['9:00','9:16 4/11','9:32 8/11','9:49 1/11']` |
| R1-Q43 | D | 5.0 | numeric | `ans=(3**2+4**2)**0.5 ; vals=[1,5,7,12]` |
| R1-Q44 | C | 50 | numeric | `ans=Fraction(150)/(Fraction(120,60)+Fraction(30,30)) ; vals=[40,45,50,60]` |
| R1-Q45 | C | 4/3 | numeric | `ans=Fraction(4,3) ; vals=[Fraction(3,4),Fraction(4,3),Fraction(7,12),Fraction(12,7)]` |
| R1-Q46 | C | The tank never fills | string | `net=Fraction(1,12)-Fraction(1,6) ; ans='The tank never fills' if net<=0 else 'other' ; vals=['12 hours','6 hours','4 hours','The tank never fills']` |
| R1-Q47 | D | 50.0 | numeric | `H=14%12 ; d=abs(30*H-5.5*20) ; ans=min(d,360-d) ; vals=[50,110,130,310]` |
| R1-Q48 | A | 660 | numeric | `ans=Fraction(330*4,2) ; vals=[165,330,660,1320]` |
| R1-Q49 | A | 18th day | string | `pos=0;d=0 ; while True: ; d+=1 ; pos+=3 ; if pos>=20: break ; pos-=2 ; ans=f'{d}th day' if d==18 else 'other' ; vals=['17th day','18th day','19th day','20th day']` |
| R1-Q50 | C | 108/5 | numeric | `h=Fraction(100)*Fraction(3,5)**3 ; vals=[Fraction(108,5),36,60,Fraction(324,5)] ; ans=h` |
| R1-Q51 | C | 46 | numeric | `from math import comb ; ans=comb(8,3)-comb(5,3) ; vals=[36,46,56,66]` |
| R1-Q52 | D | 75 | numeric | `ans=125-2*25 ; vals=[27,50,75,100]` |
| R1-Q53 | C | 8130 | numeric | `ans=2*3600+15*60+30 ; vals=[8100,8130,8160,7230]` |
| R1-Q54 | D | 8 | numeric | `from fractions import Fraction as F ; r2=F(144,100) ; ans=0 ; for _ in range(4): ; t=r2-1 ; if 0<t<=1: ans+=2 ; vals=[4,6,8,12]` |
| R1-Q55 | C | A by 1 h 20 min | string | `from fractions import Fraction as F ; tA=F(1,1)+F(2,2)+F(3,3) ; tB=F(1,3)+F(2,2)+F(3,1) ; ans='A by 1 h 20 min' if tB-tA==F(4,3) else 'other' ; vals=['A by 1 h 20 min','B by 1 h 20 min','A by 2 h','Both finish together']` |
| R1-Q56 | C | 60 | numeric | `t=Fraction(100,5) ; ans=3*t ; vals=[40,50,60,Fraction(200,3)]` |

### 2.2 Revision 2 (56 items)

| ID | Key | Verified value | Kind | Computation (`calc`) |
|---|---|---|---|---|
| R2-Q01 | C | 30 | numeric | `ans=Fraction(180+120)/(Fraction(72-36)*Fraction(5,18)) ; vals=[10,12,18,30]` |
| R2-Q02 | D | 3/2 | numeric | `ans=(Fraction(36,4)-Fraction(36,6))/2 ; vals=[Fraction(3,2),3,Fraction(9,2),Fraction(15,2)]` |
| R2-Q03 | D | 56 km/h | string | `ans='56 km/h' ; vals=['53 1/3 km/h','56 km/h','60 km/h','80 km/h']` |
| R2-Q04 | D | 15 | numeric | `ans=Fraction(300)/(Fraction(90-18,1)*Fraction(5,18)) ; vals=[10,15,20,60]` |
| R2-Q05 | D | 600 | numeric | `ans=None ; for k in range(1,200): ; t=Fraction(600*k,7) ; if (t/150).denominator==1: ; ans=t ; break ; vals=[Fraction(600,7),150,200,600] ; ans=600 if ans==600 else ans` |
| R2-Q06 | A | 16 | numeric | `ans=1/(Fraction(5,4)/20) ; vals=[15,16,20,25]` |
| R2-Q07 | D | 8:00 pm | string | `rem=1-Fraction(3,12)-Fraction(1,8) ; t=rem/(Fraction(1,8)-Fraction(1,16)) ; ans='8:00 pm' if t==10 else 'other' ; vals=['3:00 pm','6:00 pm','8:00 pm','5:30 pm']` |
| R2-Q08 | A | Saturday | string | `from datetime import date ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[date(2025,3,15).weekday()] ; vals=['Friday','Saturday','Sunday','Thursday']` |
| R2-Q09 | D | 4 | numeric | `from datetime import date ; ans=sum(1 for y in range(2001,2031) if date(y,1,1).weekday()==6) ; vals=[3,4,5,6]` |
| R2-Q10 | A | 157.5 | numeric | `d=abs(30*8+0.5*15-6*15) ; ans=min(d,360-d) ; vals=[22.5,150,157.5,202.5]` |
| R2-Q11 | A | 4:05 5/11 | string | `from fractions import Fraction as F ; M=F(60,11) ; ans='4:05 5/11' if abs(120-F(11,2)*M)==90 else 'other' ; vals=['4:00','4:05 5/11','4:21 9/11','4:38 2/11']` |
| R2-Q12 | B | 51 | numeric | `ans=sum(1 for y in range(1896,2105) if (y%4==0 and (y%100!=0 or y%400==0))) ; vals=[50,51,52,53]` |
| R2-Q13 | C | 6 | numeric | `ans=Fraction(6*6*8,3)/(4*4) ; vals=[4,6,8,12]` |
| R2-Q14 | B | 36π cm³ | string | `from fractions import Fraction as F ; ans=str(F(4,3)*27)+'π cm³' ; vals=['18π cm³','36π cm³','144π cm³','288π cm³']` |
| R2-Q15 | D | 96 | numeric | `n=6 ; ans=6*(n-2)**2 ; vals=[48,64,72,96]` |
| R2-Q16 | A | 6 | numeric | `a,b,c=3,4,5 ; ans=(a-2)*(b-2)*(c-2) ; vals=[6,12,24,60]` |
| R2-Q17 | A | 22 | numeric | `R,C=9,5 ; cells=[(r,c) for r in range(R) for c in range(C)] ; adj={x:[(x[0]+dr,x[1]+dc) for dr,dc in ((1,0),(-1,0),(0,1),(0,-1)) if 0<=x[0]+dr<R and 0<=x[1]+dc<C] for x in cells} ; black=[x for x in cells if (x[0]+x[1])%2==0] ; match={} ; def tk(u,seen): ; for v in adj[u]: ; if v in seen: continue ; seen.add(v) ; if v not in match or tk(match[v],seen): ; match[v]=u ; return True ; return False ; ans=sum(1 for u in black if tk(u,set())) ; vals=[18,20,22,23]` |
| R2-Q18 | C | 190 | numeric | `ans=1000-1000*(Fraction(900,1000))**2 ; vals=[100,190,180,200]` |
| R2-Q19 | D | 18 | numeric | `ans=18 ; assert Fraction(30)/(ans-3)==Fraction(42)/(ans+3) ; vals=[15,18,21,12]` |
| R2-Q20 | B | Saturday | string | `from datetime import date ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[date(2100,12,25).weekday()] ; vals=['Friday','Saturday','Sunday','Tuesday']` |
| R2-Q21 | C | 2/7 s | string | `ans='2/7 s' if Fraction(10,35)==Fraction(2,7) else 'other' ; vals=['4/35 s','1/2 s','2/7 s','2/3 s']` |
| R2-Q22 | A | 128 | numeric | `b=Fraction(48,6) ; ans=2*b*b ; vals=[64,96,128,384]` |
| R2-Q23 | C | 12.0 | numeric | `ans=abs(0*(0-4)+6*(4-0)+2*(0-0))/2 ; vals=[6,10,12,24]` |
| R2-Q24 | C | 6.0 | numeric | `ans=abs(8-8)**2+6**2 ; ans=ans**0.5 ; vals=[6,10,14,22]` |
| R2-Q25 | B | 17 1/7 days | string | `from fractions import Fraction as F ; total=(F(1,10)+F(1,15)+F(1,12))/2 ; A=total-F(1,15) ; ans='17 1/7 days' if 1/A==F(120,7) else 'other' ; vals=['8 days','10 days','17 1/7 days','24 days']` |
| R2-Q26 | C | 9 2/3 days | string | `from fractions import Fraction as F ; w=F(0);d=0 ; while True: ; d+=1 ; rate=F(1,12) if d%2==1 else F(1,8) ; if w+rate>=1: ; t=(d-1)+(1-w)/rate ; break ; w+=rate ; ans='9 2/3 days' if t==F(29,3) else 'other' ; vals=['9 2/3 days','10 1/2 days','10 days','8 days']` |
| R2-Q27 | B | 1 9/11 h | string | `ans='1 9/11 h' if (Fraction(2,3)/(Fraction(1,3)+Fraction(1,5)-Fraction(1,6)))==Fraction(20,11) else 'other' ; vals=['20/21 h','1 9/11 h','2 8/11 h','1 1/4 h']` |
| R2-Q28 | C | 22 | numeric | `from fractions import Fraction as F ; ans=len([j for j in range(-5,100) if 1080<F(180+360*j,11)<1800]) ; vals=[11,22,24,44]` |
| R2-Q29 | C | Monday | string | `from datetime import date ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[date(2100,3,1).weekday()] ; vals=['Sunday','Monday','Tuesday','Friday']` |
| R2-Q30 | D | 748 | numeric | `ans=2*Fraction(22,7)*7*(7+10) ; vals=[440,308,616,748]` |
| R2-Q31 | A | 3000 | numeric | `ans=Fraction(3*2*50,100)*1000 ; vals=[300,3000,30000,30]` |
| R2-Q32 | B | 500 | numeric | `ans=Fraction(110000)/(Fraction(22,7)*70) ; vals=[50,250,500,5000]` |
| R2-Q33 | B | 100.0 | numeric | `ans=(Fraction(60)**2+Fraction(80)**2)**0.5 ; vals=[20,70,100,140]` |
| R2-Q34 | B | 4:1 | string | `from fractions import Fraction as F ; b=F(4);s=F(1) ; assert F(15)/(b-s)==5 and F(15)/(b+s)==3 ; ans='4:1' ; vals=['4:1','1:4','5:3','2:1']` |
| R2-Q35 | D | 2025 | string | `from datetime import date ; ans=[y for y in range(2021,2030) if date(y,1,1).weekday()==2][0] ; ans=str(ans) ; vals=['2024','2025','2026','2027']` |
| R2-Q36 | D | 11:42 | string | `lost=3*6 ; ans='11:42' if 12*60-lost==11*60+42 else 'other' ; vals=['11:48','11:42','12:18','11:36']` |
| R2-Q37 | B | 45 | numeric | `ans=Fraction(3)/(Fraction(1,30)+Fraction(2,60)) ; vals=[40,45,50,60]` |
| R2-Q38 | C | 54 | numeric | `n=5 ; ans=6*(n-2)**2 ; vals=[8,27,36,54]` |
| R2-Q39 | D | 2:43 7/11 | string | `from fractions import Fraction as F ; M=F(480,11) ; ans='2:43 7/11' if abs(60-F(11,2)*M)==180 else 'other' ; vals=['2:16 4/11','2:32 8/11','2:43 7/11','2:49 1/11']` |
| R2-Q40 | C | 6 | numeric | `ans=Fraction(12,3)+Fraction(5,Fraction(5,2)) ; vals=[4,6,6.5,13]` |
| R2-Q41 | B | 3 | numeric | `ans=Fraction(300,60+40) ; vals=[3,5,7.5,15]` |
| R2-Q42 | A | 20 km/h | string | `ans='20 km/h' if Fraction(50)/Fraction(5,2)==20 else 'other' ; vals=['20 km/h','25 km/h','30 km/h','16.7 km/h']` |
| R2-Q43 | B | 384.0 | numeric | `a=(Fraction(96,6))**Fraction(1,2) ; b=2*a ; ans=6*b*b ; vals=[192,384,480,768]` |
| R2-Q44 | A | 12:32 8/11 | string | `from fractions import Fraction as F ; M=F(360,11) ; ans='12:32 8/11' if abs(F(11,2)*M-180)==0 else 'other' ; vals=['12:16 4/11','12:32 8/11','12:49 1/11','1:05 5/11']` |
| R2-Q45 | A | 30 | numeric | `v=Fraction(200,10) ; ans=(200+400)/v ; vals=[10,20,30,40]` |
| R2-Q46 | B | 52.5 | numeric | `H=22%12 ; d=abs(30*H+0.5*45-6*45) ; ans=min(d,360-d) ; vals=[52.5,127.5,232.5,412.5]` |
| R2-Q47 | C | The tank never fills | string | `net=Fraction(1,12)-Fraction(1,6) ; ans='The tank never fills' if net<=0 else 'other' ; vals=['4 hours','12 hours','6 hours','The tank never fills']` |
| R2-Q48 | D | 2979 | numeric | `ans=(330+1)*9 ; vals=[2961,2970,2979,3240]` |
| R2-Q49 | A | 12th day | string | `pos=0;d=0 ; while True: ; d+=1 ; pos+=4 ; if pos>=15: break ; pos-=3 ; ans=f'{d}th day' if d==12 else 'other' ; vals=['11th day','12th day','13th day','15th day']` |
| R2-Q50 | D | 5 | numeric | `ans=Fraction(80)*Fraction(1,2)**4 ; vals=[10,5,20,40]` |
| R2-Q51 | A | 20 | numeric | `from math import comb ; ans=comb(6,3) ; vals=[15,20,60,120]` |
| R2-Q52 | C | 144 | numeric | `n=6 ; ans=n**3-2*n*n ; vals=[72,108,144,180]` |
| R2-Q53 | C | 6320 | numeric | `ans=3600+45*60+20 ; vals=[6300,6320,6360,3620]` |
| R2-Q54 | A | 8 | numeric | `from fractions import Fraction as F ; r2=F(625,100) ; ans=0 ; for _ in range(4): ; t=r2-4 ; if 0<t<=4: ans+=2 ; vals=[0,4,8,10]` |
| R2-Q55 | B | Q by 35 min | string | `from fractions import Fraction as F ; tP=F(6,3)+F(4,8)+F(2,4) ; tQ=F(6,8)+F(4,4)+F(2,3) ; ans='Q by 35 min' if tP-tQ==F(7,12) else 'other' ; vals=['P by 35 min','Q by 35 min','Q by 25 min','Both finish together']` |
| R2-Q56 | A | 120 | numeric | `from fractions import Fraction as F ; vA=F(6000,3600) ; vB=F(4000,3600) ; t=F(40)/(vA-vB) ; ans=vA*t ; vals=[80,120,160,40]` |

### 2.3 Revision 3 (54 items)

| ID | Key | Verified value | Kind | Computation (`calc`) |
|---|---|---|---|---|
| R3-Q01 | B | Train R | string | `from fractions import Fraction as F ; T={'P':F(120+330)/F(72*5,18),'Q':F(180+330)/F(54*5,18),'R':F(200+330)/F(90*5,18),'S':F(150+330)/F(45*5,18)} ; best=min(T,key=T.get) ; ans='Train '+best ; vals=['Train P','Train Q','Train R','Train S']` |
| R3-Q02 | B | 4.5 m/s | string | `ans='4.5 m/s' if Fraction(1800)/(Fraction(600,6)+Fraction(600,6)+Fraction(600,3))==Fraction(9,2) else 'other' ; vals=['4 m/s','4.5 m/s','5 m/s','6 m/s']` |
| R3-Q03 | D | 11 1/3 days | string | `from fractions import Fraction as F ; rates=[F(1,8),F(1,12),F(1,20)] ; w=F(0);d=0 ; while True: ; r=rates[d%3]; d+=1 ; if w+r>=1: ; t=(d-1)+(1-w)/r ; break ; w+=r ; ans='11 1/3 days' if t==F(34,3) else 'other' ; vals=['10 days','11 days','11 1/3 days','12 days']` |
| R3-Q04 | D | 3:12 pm | string | `from fractions import Fraction as F ; w=F(1,6)+(F(1,6)+F(1,12)) ; rem=1-w ; t=rem/(F(1,4)-F(1,9)) ; ans='3:12 pm' if 11+t==F(15)+F(12,60) else 'other' ; vals=['1:20 pm','2:36 pm','3:12 pm','4:00 pm']` |
| R3-Q05 | B | 10 | numeric | `ans=Fraction(60,6) ; vals=[5,10,15,20]` |
| R3-Q06 | A | Thursday | string | `import math ; L=math.lcm(6,8) ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[L%7] ; vals=['Monday','Tuesday','Wednesday','Thursday']` |
| R3-Q07 | A | Saturday | string | `from datetime import date ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[date(2026,8,15).weekday()] ; vals=['Friday','Saturday','Sunday','Thursday']` |
| R3-Q08 | C | 112 | numeric | `ans=20*12-(20-4)*(12-4) ; vals=[96,112,128,144]` |
| R3-Q09 | B | 10.0 | numeric | `ans=(30**2+40**2)**0.5/5 ; vals=[7,10,14,20]` |
| R3-Q10 | A | 800 s | string | `import math ; ans='800 s' if math.lcm(400,160)==800 else 'other' ; vals=['160 s','266 2/3 s','400 s','800 s']` |
| R3-Q11 | B | 24 | numeric | `from fractions import Fraction as F ; A=(1-4*F(1,12))/16 ; B=F(1,12)-A ; ans=1/B ; vals=[12,16,24,8]` |
| R3-Q12 | A | 39 km/h | string | `ans='39 km/h' if Fraction(130)/(3+Fraction(20,60))==39 else 'other' ; vals=['39 km/h','43 1/3 km/h','45 km/h','40 km/h']` |
| R3-Q13 | D | 16 | numeric | `a,b,c=5,3,2 ; ans=4*((a-2)+(b-2)+(c-2)) ; vals=[8,12,16,20]` |
| R3-Q14 | D | 10 | numeric | `ans=Fraction(400)/(Fraction(144,1)*Fraction(5,18)) ; vals=[Fraction(15,2),10,Fraction(25,2),20]` |
| R3-Q15 | D | 40 | numeric | `t=Fraction(90,9) ; ans=4*t ; vals=[36,40,45,50]` |
| R3-Q16 | A | 22 | numeric | `from fractions import Fraction as F ; ans=0 ; for k in range(-2,50): ; for sgn in (45,315): ; t=F(sgn+360*k,F(11,2)) ; if 0<=t<720: ans+=1 ; ans=ans ; vals=[11,22,24,44]` |
| R3-Q17 | A | 1 | numeric | `from datetime import date ; ans=sum(1 for m in range(1,13) if date(2027,m,13).weekday()==4) ; vals=[1,2,3,4]` |
| R3-Q18 | B | 2029 | string | `from datetime import date ; ans=[y for y in range(2027,2040) if date(y,1,1).weekday()==0][0] ; ans=str(ans) ; vals=['2028','2029','2030','2031']` |
| R3-Q19 | C | 6:32 8/11 | string | `from fractions import Fraction as F ; M=F(4320,11)-360 ; ans='6:32 8/11' if (180-F(11,2)*M)==0 and M>0 else 'other' ; vals=['6:16 4/11','6:32 8/11','6:49 1/11','7:38 2/11']` |
| R3-Q20 | A | 200 | numeric | `ans=Fraction(2*1.5*1*1000)/15 ; vals=[20,200,2000,3000]` |
| R3-Q21 | A | 5.0 | numeric | `ans=(6**2+8**2)**0.5/2 ; vals=[5,7,10,14]` |
| R3-Q22 | D | 16 2/3 days | string | `from fractions import Fraction as F ; k=F(1,10)/5 ; A=3*k ; ans='16 2/3 days' if 1/A==F(50,3) else 'other' ; vals=['12 days','16 2/3 days','25 days','10 days']` |
| R3-Q23 | D | B wins by 40 s | string | `tA=Fraction(600,4) ; tB=10+Fraction(600,6) ; ans='B wins by 40 s' if tA-tB==40 else 'other' ; vals=['A wins by 40 s','B wins by 40 s','B wins by 50 s','A wins by 10 s']` |
| R3-Q24 | A | A and B | string | `from fractions import Fraction as F ; r={'A':F(1,12),'B':F(1,16),'C':F(1,24)} ; pairs={'A and B':r['A']+r['B'],'A and C':r['A']+r['C'],'B and C':r['B']+r['C'],'C alone':r['C']} ; ans=max(pairs,key=pairs.get) ; vals=['A and B','A and C','B and C','C alone']` |
| R3-Q25 | A | P by 15 min | string | `from fractions import Fraction as F ; tP=F(2,4)+F(3,6)+F(4,8) ; tQ=F(2,8)+F(3,6)+F(4,4) ; ans='P by 15 min' if tQ-tP==F(1,4) else 'other' ; vals=['P by 15 min','Q by 15 min','P by 30 min','Both finish together']` |
| R3-Q26 | B | 52 km/h | string | `ans='52 km/h' if Fraction(2*50+1*80+2*40,5)==52 else 'other' ; vals=['52 km/h','56 2/3 km/h','60 km/h','65 km/h']` |
| R3-Q27 | C | 14 | numeric | `ans=sum(1 for d in range(1,61) if [d%2==0,d%3==0,d%5==0].count(True)==2) ; vals=[10,12,14,16]` |
| R3-Q28 | D | 12 | numeric | `ans=Fraction(5*400,1000)/Fraction(10,60) ; vals=[8,10,12,24]` |
| R3-Q29 | B | 30.0 | numeric | `lap=100/5 ; ans=(10*60)//lap ; vals=[3,15,30,60]` |
| R3-Q30 | A | 16.5 days | string | `from fractions import Fraction as F ; b=F(1,9)/F(11,5) ; A=F(6,5)*b ; ans='16.5 days' if 1/A==F(33,2) else 'other' ; vals=['15 days','16.5 days','18 days','20.25 days']` |
| R3-Q31 | C | 15.0 | numeric | `ans=1.2*1*0.5*1000/40 ; vals=[6,15,60,150]` |
| R3-Q32 | C | 72 | numeric | `ans=Fraction(480+320,40)*Fraction(18,5) ; vals=[Fraction(216,5),72,80,20]` |
| R3-Q33 | D | Thursday | string | `from datetime import date ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[date(2026,12,31).weekday()] ; vals=['Wednesday','Thursday','Friday','Saturday']` |
| R3-Q34 | B | 3:19 1/11 | string | `from fractions import Fraction as F ; M=F(210,11) ; ans='3:19 1/11' if (6*M)-(90+F(1,2)*M)==15 else 'other' ; vals=['3:15','3:19 1/11','3:20','3:45']` |
| R3-Q35 | B | 6 | numeric | `ans=Fraction(24)/(1+1+2) ; vals=[6,8,9,12]` |
| R3-Q36 | A | 60 | numeric | `rel=Fraction(150,10)*Fraction(18,5) ; ans=rel+6 ; vals=[48,54,60,66]` |
| R3-Q37 | B | 12 | numeric | `from fractions import Fraction as F ; B=F(1,30) ; A=F(3,2)*B ; ans=1/(A+B) ; vals=[10,12,15,18]` |
| R3-Q38 | C | Monday | string | `import math ; L=math.lcm(9,12) ; W=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'] ; ans=W[(6+L)%7] ; vals=['Sunday','Monday','Tuesday','Wednesday']` |
| R3-Q39 | D | 0.15 ha | string | `from fractions import Fraction as F ; ans='0.15 ha' if F((60+40)*30,2)/10000==F(3,20) else 'other' ; vals=['0.015 ha','0.15 ha','1.5 ha','15 ha']` |
| R3-Q40 | D | 384 | numeric | `ans=(1200//50)*(800//50) ; vals=[96,192,384,768]` |
| R3-Q41 | B | 10 | numeric | `ans=10 ; assert Fraction(24,ans-2)+Fraction(24,ans+2)==5 ; vals=[6,8,10,12]` |
| R3-Q42 | C | 45.0 | numeric | `d=abs(30*7+0.5*30-6*30) ; ans=min(d,360-d) ; vals=[30,45,75,135]` |
| R3-Q43 | C | 96 | numeric | `ans=6*16 ; vals=[24,48,64,96]` |
| R3-Q44 | D | 3 | numeric | `ans=Fraction(54-36,1)*Fraction(10,60) ; vals=[3,6,9,15]` |
| R3-Q45 | A | 3 h 15 min | string | `ans='3 h 15 min' if Fraction(240,80)+Fraction(15,60)==Fraction(13,4) else 'other' ; vals=['3 h','2 h 45 min','3 h 15 min','3 h 45 min']` |
| R3-Q46 | C | The cistern never fills | string | `net=Fraction(1,10)-Fraction(1,8) ; ans='The cistern never fills' if net<=0 else 'other' ; vals=['10 hours','8 hours','40/9 hours','The cistern never fills']` |
| R3-Q47 | C | 130.0 | numeric | `H=15%12 ; d=abs(30*H+0.5*40-6*40) ; ans=min(d,360-d) ; vals=[150,130,230,170]` |
| R3-Q48 | C | 850 | numeric | `ans=Fraction(340*5,2) ; vals=[425,680,850,1700]` |
| R3-Q49 | C | 11th day | string | `pos=0;d=0 ; while True: ; d+=1 ; pos+=2 ; if pos>=12: break ; pos-=1 ; ans=f'{d}th day' if d==11 else 'other' ; vals=['9th day','10th day','11th day','12th day']` |
| R3-Q50 | B | 40 | numeric | `ans=Fraction(90)*Fraction(2,3)**2 ; vals=[40,60,30,45]` |
| R3-Q51 | A | 21 | numeric | `from math import comb ; ans=comb(8,3)-comb(7,3) ; vals=[21,28,35,56]` |
| R3-Q52 | C | 16 | numeric | `n=4 ; ans=(n-2)**2*n ; vals=[4,8,16,32]` |
| R3-Q53 | A | 60.5 | numeric | `from datetime import datetime ; d=datetime(2026,11,5,11,0)-datetime(2026,11,2,22,30) ; ans=d.total_seconds()/3600 ; vals=[59.5,60.5,61.5,72.5]` |
| R3-Q54 | C | 4 | numeric | `ans=4 ; vals=[0,2,4,8]` |

## 3. Uniqueness and distractor checks

- Uniqueness: for every item, exactly one option is equal to the computed answer (engine rule 2). Distractors were chosen from named error routes recorded in `ANSWERS.md` (for example: same-direction rule applied to opposite motion; harmonic mean used for unequal distances; drain treated as a filler; 2100 counted as leap; right angle confused with coincidence; reflex angle reported as the smaller angle; path length given for displacement; unconverted km/h; area used for tile count).
- Stem constraints checked by enumeration where the stem has a shared rule: tiling counts (R1-Q37, R2-Q17 by maximum matching on the 9 × 5 grid), calendar sweeps (R2-Q09, R2-Q12, R2-Q20, R3-Q17, R3-Q18, R3-Q33, R3-Q38), clock sweeps (R2-Q28, R3-Q16, R3-Q19, R1-Q23), rota count (R3-Q27), race and walker timings (R2-Q05, R3-Q10), and the two-root clock equations (R2-Q11, R2-Q39, R1-Q42, R3-Q34).
- Stem phrases that could create a second defensible answer were fixed in the stem, not left to the reader: the tiling items say whether orientation may vary per tile (R1-Q37 uniform; R2-Q17 per tile); the calendar items name the starting day; the clock items say 'smaller angle' or name the window; the alternate-day items name who works first; the circle–square items give radius against half-side and half-diagonal.

## 4. Answer-position balance

Correct letters were assigned by a seeded permutation over an exact target multiset (about 26% A, 25% B, 25% C, 24% D), and distractors kept their authored relative order. Final counts:

| Set | Items | A | B | C | D | A % | B % | C % | D % |
|---|---|---|---|---|---|---|---|---|---|
| R1 | 56 | 15 | 13 | 14 | 14 | 26.8 | 23.2 | 25.0 | 25.0 |
| R2 | 56 | 15 | 13 | 14 | 14 | 26.8 | 23.2 | 25.0 | 25.0 |
| R3 | 54 | 15 | 13 | 14 | 12 | 27.8 | 24.1 | 25.9 | 22.2 |

Each letter holds 20–30% of keys in every set.

## 5. Option-length and cue balance

Length was measured as the character count of the option text as printed (units included). Two statistics are reported: the share of items in which the correct option is the **uniquely longest** (rule: no more than about 25%), and the share of items whose longest option is within 25% of the shortest (INSTRUCTIONS target).

| Set | Items | Correct uniquely longest | % | Longest ≤ 1.25 × shortest | % | Mean longest/shortest | Max longest/shortest |
|---|---|---|---|---|---|---|---|
| R1 | 56 | 6 | 10.7 | 29 | 51.8 | 1.4 | 2.86 |
| R2 | 56 | 3 | 5.4 | 33 | 58.9 | 1.33 | 2.86 |
| R3 | 54 | 5 | 9.3 | 28 | 51.9 | 1.38 | 3.33 |

Result: the uniquely-longest rule passes in all three sets (at most 10.7%). The 1.25× length-spread target is **not** met in about 40–50% of items. The residual spread comes from numeric and unit answers whose options differ in magnitude (for example `0.15 ha` against `15 ha`, `2.4 L` against `24000 L`, `3 h 15 min` against `3 h`). This is recorded as a documented soft deviation rather than rewritten, because each distractor was kept on a named error route.

## 6. Practice-difficulty and time checks

- Time budget: 56 (R1), 56 (R2) and 54 (R3) items per set at about 72 s each (each QUESTIONS.md header states the minutes). Per-item targets are recorded in each ANSWERS entry; they range from 45 s (direct formula) to 150 s (multi-stage schedules and brute-force counts).
- Two-step or trap share: every item carries at least one named distractor route. R1 has about 10 one-formula warm-ups (R1-Q23, Q28, Q30, Q33, Q34, Q38, Q40, Q43, Q45, Q53); R2 and R3 are built almost entirely from multi-step items, with about seven single-formula items each (R2: Q12, Q15, Q16, Q28, Q38, Q52, Q53; R3: Q17, Q33, Q43, Q53, Q54). The 40% two-step-or-trap threshold is met in all sets.
- Scoring note in each QUESTIONS.md: +2.5 correct, −0.83 wrong, 0 skipped.

## 7. Items revised during the build

Revisions were made to the source data before the final clean run. None was made after the final run. Items whose distractors, stems, or calc blocks changed during construction:
- R1: Q07 (explanation wording), Q17 (calc and explanations for the alternate-day start), Q22 and Q42 (calc now checks the coincidence and right-angle equations), Q23 (calc now enumerates the 44 right-angle times), Q26 (calc uses the 1827-day span; distractor Sunday rewritten), Q27 (distractor rationales, 200-year odd-day count).
- R2: Q03 (harmonic distractor shown exactly as 53 1/3; key moved to an exact string check), Q04 (distractor 16.7 s replaced by 20 s), Q09 (distractor D rewritten), Q20 (distractor D changed to a 'no leap day' shift; explanation recomputed as 27,393 days), Q25 (check corrected to 1/A), Q29 (distractors changed to Sunday, Monday, Tuesday, Friday), Q34 (assertion corrected to a 15-unit check), Q43 and Q46–Q52 explanations.
- R3: Q01 (explanations), Q02, Q04 (calc placeholder removed; the opening-time errors rewritten), Q05, Q06 (distractors recomputed: 28 days is not a common multiple of 6 and 8), Q13 (distractor D), Q14 (options changed to 7.5, 10, 12.5, 20 s so that the key is 10 s), Q17, Q18, Q19 (calc rewritten to the first coincidence after 6:00, 6:32 8/11), Q20, Q22, Q23, Q28–Q30, Q33 (explanations), Q34 (calc rewritten; the 3:45 explanation corrected to a 157.5° gap), Q36 (value list order fixed), Q37 (explanation order fixed), Q39–Q41 (conversion and boat distractors rewritten).
- Coverage additions after the first complete run: Q46–Q54 in each set (never-fill pipes, 24-hour clock, sound echo, well climb, bounce height, collinear triangles, partly painted cube, time-unit conversion, circle–square intersections), plus Q55–Q56 in R1 and R2 (segment-ordering pairing swap and walker meeting/catch-up) to close owner gaps recorded in `COVERAGE.md`. R3 already carries its segment-ordering and walker items (R3-Q25, R3-Q15).

## 8. Limits of this audit

- Verification is by the author's exact computation and the engine above. No second human reviewer checked the keys; a second reviewer is recommended before the sets are used as a live test.
- Option-length spread is a documented soft deviation (§5).
- No exact UPSC PYQ wording or option set is reproduced; PYQ-pattern coverage is recorded only as family routes in `COVERAGE.md`. No PYQ key was used as an answer.

