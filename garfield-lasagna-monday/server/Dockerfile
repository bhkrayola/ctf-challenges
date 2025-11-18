FROM python:3.9-slim-buster

RUN python3 -m pip install requests flask gunicorn --no-cache-dir
WORKDIR /app 
COPY ./ ./

VOLUME ["/tmp"]

CMD ["gunicorn", "-w2", "-t4", "--graceful-timeout", "0", "-b0.0.0.0:5000", "app:app"]
