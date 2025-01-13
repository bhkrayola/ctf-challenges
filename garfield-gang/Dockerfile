FROM pwn.red/jail:0.3.0
COPY --from=ubuntu / /srv

COPY chall /srv/app/run
COPY flag.txt /srv/app/
RUN chmod +x /srv/app/run
