FROM python:3.7-stretch
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["/usr/local/bin/gunicorn", "-t", "500", "--worker-class", "eventlet", "-w", "2", "--access-logfile", "-", "-b", "0.0.0.0:5000", "app:app"]
