from flask import abort, make_response
from config import db
from models import Job, JobSchema


def read_all():
    job = Job.query.order_by(Job.job_id).all()

    job_schema = JobSchema(many=True)
    data = job_schema.dump(job)
    return data


def read_one(job_id):
    job = (
        Job.query.filter(Job.job_id == job_id)
        .one_or_none()
    )

    if job is not None:
        job_schema = JobSchema()
        data = job_schema.dump(job)
        return data

    else:
        abort(
            404, "Job with ID {job_id} not found".format(job_id=job_id)
        )


def create(job):
    # app_name = job.get("app_name")
    # state = job.get("state")
    schema = JobSchema()
    new_job = schema.load(job, session=db.session)

    db.session.add(new_job)
    db.session.commit()

    data = schema.dump(new_job)

    return data, 201


def update(job_id, job):
    update_job = Job.query.filter(
        Job.job_id == job_id
    ).one_or_none()



    if update_job is not None:
        schema = JobSchema()
        up = schema.load(job, session=db.session)
        up.job_id = update_job.job_id

        db.session.merge(up)
        db.session.commit()
        data = schema.dump(update_job)

        return data, 200
    else:
        abort(404, f"Job not found for Id: {job_id}")


def delete(job_id):
    job = Job.query.filter(Job.job_id == job_id).one_or_none()

    if job is not None:
        db.session.delete(job)
        db.session.commit()
        return make_response(f"Job {job_id} deleted", 200)

    else:
        abort(404, f"Job not found for Id: {job_id}")