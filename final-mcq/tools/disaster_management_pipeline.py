import runpy, sys
sys.argv = [sys.argv[0], "Disaster-Management"]
runpy.run_path(__file__.replace("disaster_management_pipeline.py", "subject_release_pipeline.py"), run_name="__main__")
