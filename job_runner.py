import os
import time

def run_job(job_id):
    os.system(f"echo {job_id} > job_id.txt")
    os.system(f"git add job_id.txt")
    os.system(f"git commit -m \"run job {job_id}\"")
    os.system("git push origin")
    print(f"Started job {job_id}")


job_id = 1
while True:
    run_job(job_id)
    job_id+=1
    time.sleep(60*20)

