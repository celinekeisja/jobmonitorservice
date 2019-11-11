from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import db
import config

app = config.connex_app

app.add_api('swagger.yml')

@app.route('/')
def home():
    return 'homepage here'

@app.route("/job")
@app.route("/job/<string:job_id>")
def job(job_id=""):
    return 'result of job_id'


migrate = Migrate(app=app, db=db)
manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

if __name__ == "__main__":
    manager.run()
    # app.run(host='localhost', port=5000, debug=True)