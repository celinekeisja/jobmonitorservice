FROM python:3

WORKDIR /app

ADD . /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask gunicorn
EXPOSE 8080
CMD ["gunicorn", "server:app", "-b", "0.0.0.0:8080"]
