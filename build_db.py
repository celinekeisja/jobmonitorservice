import os
from config import db
from models import Job

JOBS = [
    {'job_id ': '{uuid.uuid1()}', 'app_name': 'Telegram', 'state': 'PROCESSING'},
    {'job_id ': '{uuid.uuid1()}', 'app_name': 'Name1', 'state': 'PROCESSING'}

]

if os.path.exists("modulelogs.db"):
    os.remove("modulelogs.db")

db.create_all()

for job in JOBS:
    j = Job(job_id=job.get("job_id"), app_name=job.get("app_name"), state=job.get("state"))

    db.session.add(j)

db.session.commit()