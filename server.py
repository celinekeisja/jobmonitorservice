from flask import Flask
import config

app = config.connex_app

app.add_api('swagger.yml')

# Create a URL route in our application for "/"
@app.route('/')
def home():
    """
    This function just responds to the browser ULR
    localhost:5000/
    """
    return 'homepage here'

@app.route("/job")
@app.route("/job/<string:job_id>")
def job(job_id=""):
    """
    This function just responds to the browser URL
    localhost:5000/people
    :return:        the rendered template "people.html"
    """
    return 'result of job_id'

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)