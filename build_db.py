import os
from config import db
from models import Job

# Data to initialize database with
JOBS = [
    {'job_id ': '{uuid.uuid1()}', 'app_name': 'Telegram', 'state': 'PROCESSING'},
    {'job_id ': '{uuid.uuid1()}', 'app_name': 'Name1', 'state': 'PROCESSING'}

]

# Delete database file if it exists currently
if os.path.exists("modulelogs.db"):
    os.remove("modulelogs.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for job in JOBS:
    j = Job(job_id=job.get("job_id"), app_name=job.get("app_name"), state=job.get("state"))

    db.session.add(j)

db.session.commit()