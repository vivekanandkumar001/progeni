# simple stub to create sample jobs.json
import json
jobs = [
    {"id":1, "title":"Data Scientist", "company":"ABC", "location":"Remote", "description":"Python, ML", "url":"https://example.com/job/1"},
    {"id":2, "title":"Software Engineer", "company":"XYZ", "location":"Delhi", "description":"Backend, Python", "url":"https://example.com/job/2"}
]
with open('jobs.json','w') as f:
    json.dump(jobs, f, indent=2)
print("jobs.json created")
