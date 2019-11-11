from flask import Flask
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


if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)