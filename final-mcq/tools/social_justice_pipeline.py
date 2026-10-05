import runpy, sys
sys.argv = [sys.argv[0], "Social-Justice"]
runpy.run_path(__file__.replace("social_justice_pipeline.py", "subject_release_pipeline.py"), run_name="__main__")
