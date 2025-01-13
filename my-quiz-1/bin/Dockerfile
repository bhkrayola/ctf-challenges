FROM pwn.red/jail:0.3.0
COPY --from=python:3.8 / /srv
COPY main.py /srv/app/run
COPY flag.txt /srv/app/
RUN chmod +x /srv/app/run