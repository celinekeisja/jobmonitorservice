from flask import make_response, abort
from config import db
from models import Job, JobSchema

# Create a handler for our read (GET) people
def read_all():
    """
    This function responds to a request for /api/people
    with the complete lists of people
    :return:        json string of list of people
    """
    # Create the list of people from our data
    job = Job.query.order_by(Job.job_id).all()

    # Serialize the data for the response
    job_schema = JobSchema(many=True)
    data = job_schema.dump(job)
    return data


def read_one(job_id):
    """
    This function responds to a request for /api/people/{lname}
    with one matching person from people
    :param lname:   last name of person to find
    :return:        person matching last name
    """

    # Get the person requested
    job = (
        Job.query.filter(Job.job_id == job_id)
        .one_or_none()
    )
    # Did we find a person?
    if job is not None:

        # Serialize the data for the response
        job_schema = JobSchema()
        data = job_schema.dump(job)
        return data

    # otherwise, nope, not found
    else:
        abort(
            404, "Job with ID {job_id} not found".format(job_id=job_id)
        )


def create(job):
    """
    This function creates a new person in the people structure
    based on the passed in person data
    :param person:  person to create in people structure
    :return:        201 on success, 406 on person exists
    """
    # job_id = job.get("job_id")
    app_name = job.get("app_name")
    state = job.get("state")

    # Does the person exist already?
    # existing_job = (
    #     Job.query.filter(Job.job_id == job_id)
    #     .one_or_none()
    # )

    # Can we insert this person?
    # if existing_job is None:

        # Create a person instance using the schema and the passed in person
    schema = JobSchema()
    new_job = schema.load(job, session=db.session)

    # Add the person to the database
    db.session.add(new_job)
    db.session.commit()

    # Serialize and return the newly created person in the response
    data = schema.dump(new_job)

    return data, 201

    # Otherwise, they exist, that's an error
    # else:
    #     abort(
    #         409,
    #         "Job with ID {job_id} already exists".format(job_id=job_id),
    #     )

#
# def update(job_id):
#     """
#     This function updates an existing person in the people structure
#     :param lname:   last name of person to update in the people structure
#     :param person:  person to update
#     :return:        updated person structure
#     """
#     # Get the person requested from the db into session
#     update_job = Job.query.filter(
#         Job.job_id == job_id
#     ).one_or_none()
#
#     # Try to find an existing person with the same name as the update
#     if update_job is not None:
#
#         # turn the passed in person into a db object
#         schema = JobSchema()
#
#         # Set the id to the person we want to update
#         up = update.job_id == update_job.job_id
#
#         # merge the new object into the old and commit it to the db
#         db.session.merge(up)
#         db.session.commit()
#
#         # return updated person in the response
#         data = schema.dump(update_job)
#
#         return data, 200
#
#         # Otherwise, nope, didn't find that person
#     else:
#         abort(404, f"Job not found for Id: {job_id}")
#
#
# def delete(job_id):
#     """
#     This function deletes a person from the people structure
#     :param lname:   last name of person to delete
#     :return:        200 on successful delete, 404 if not found
#     """
#  # Get the person requested
#     job = Job.query.filter(Job.job_id == job_id).one_or_none()
#
#     # Did we find a person?
#     if job is not None:
#         db.session.delete(job)
#         db.session.commit()
#         return make_response(f"Job {job_id} deleted", 200)
#
#     # Otherwise, nope, didn't find that person
#     else:
#         abort(404, f"Job not found for Id: {job_id}")