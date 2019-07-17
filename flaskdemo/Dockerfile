FROM python:alpine
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn --bind 0.0.0.0:5000 --workers 10 server:app
EXPOSE 5000
