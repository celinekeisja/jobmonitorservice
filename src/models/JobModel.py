from marshmallow import fields, Schema
from . import db
import datetime
from sqlalchemy.dialects.postgresql import UUID
from .StateModel import StateSchema

class JobModel(db.Model):
    __tablename__ = 'jobs'

    pk_id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(UUID(as_uuid=True), unique=True, nullable=False)

    def __init__(self, data):

        self.job_id = data.get('job_id')

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()
        states = db.relationship('StateModel', backref='jobs', lazy=True)

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_jobs():
        return JobModel.query.all()

    @staticmethod
    def get_one_job(job_id):
        return JobModel.query.get(job_id)

    def __repr__(self):
        return '<job_id {}>'.format(self.job_id)

    class JobSchema(Schema):
        pk_id = fields.Int(dump_only=True)
        job_id = fields.UUID(required=True)