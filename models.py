from datetime import datetime
from uuid import uuid4

from config import db, ma
from sqlalchemy.dialects.postgresql import UUID


class Job(db.Model):
    __tablename__ = "job"
    pk_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    job_id = db.Column(UUID(as_uuid=True), default=uuid4, unique=True, nullable=False)
    app_name = db.Column(db.String, nullable=False)
    state = db.Column(db.String, nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class JobSchema(ma.ModelSchema):
    class Meta:
        model = Job
        sql_session = db.session
