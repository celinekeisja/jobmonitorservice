from . import db
import datetime
from marshmallow import fields, Schema
from sqlalchemy.dialects.postgresql import UUID

class StateModel(db.Model):
    __tablename__ = 'states'

    state_id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(8), nullable=False)
    app_name = db.Column(db.String(250), nullable=False)
    job_id = db.Column(UUID(as_uuid=True), db.ForeignKey('jobs.job_id'), unique=True, nullable=False)
    date_created = db.Column(db.DateTime)

    def __init__(self, data):
        self.state_id = data.get('state_id')
        self.state = data.get('state')
        self.app_name = data.get('app_name')
        self.job_id = data.get('job_id')
        self.date_created = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data):
        for key, item in data.items():
            setattr(self, key, item)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_all_states():
        return StateModel.query.all()

    @staticmethod
    def get_one_state(state_id):
        return StateModel.query.get(state_id)

    def __repr__(self):
        return '<state_id {}>'.format(self.state_id)

class StateSchema(Schema):
    state_id = fields.Int(dump_only=True)
    state = fields.Str(required=True)
    app_name = fields.Str(required=True)
    job_id = fields.UUID(required=True)
    date_created = fields.DateTime(dump_only=True)
