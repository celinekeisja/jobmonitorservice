FROM python:3
ADD . /app
WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install flask gunicorn
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "server"]