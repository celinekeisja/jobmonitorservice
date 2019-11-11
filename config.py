import os
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = os.path.abspath(os.path.dirname(__file__))

connex_app = connexion.App(__name__, specification_dir=os.path.join(basedir))

app = connex_app.app

postgres_url = 'postgres://host.docker.internal:5432/modulelogs?user=postgres&password=password'
# sqlite_url = "sqlite:////"+os.path.join(basedir, "modulelogs.db")

app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_DATABASE_URI"] = postgres_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

ma = Marshmallow(app)