import json, os
def scrape_jobs_stub():
    jobs = [
        {"id":1, "title":"Data Scientist", "company":"ABC", "location":"Remote", "description":"Python, ML", "url":"https://example.com/job/1"},
        {"id":2, "title":"Software Engineer", "company":"XYZ", "location":"Delhi", "description":"Backend, Python", "url":"https://example.com/job/2"}
    ]
    os.makedirs('data', exist_ok=True)
    with open('data/jobs.json','w') as f:
        json.dump(jobs, f, indent=2)
    return jobs
