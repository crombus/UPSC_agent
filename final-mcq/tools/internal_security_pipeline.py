import runpy, sys
sys.argv = [sys.argv[0], "Internal-Security"]
runpy.run_path(__file__.replace("internal_security_pipeline.py", "subject_release_pipeline.py"), run_name="__main__")
