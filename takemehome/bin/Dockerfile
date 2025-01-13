FROM pwn.red/jail:0.3.0
COPY --from=ubuntu / /srv

COPY run.sh /srv/app/run
RUN chmod +x /srv/app/run
COPY flag.txt /srv/flag.txt
ENV JAIL_TIME=90
