FROM ubuntu:18.04

RUN mkdir -p /opt/app
WORKDIR /opt/app

COPY client-cert.pem client-key.pem server-ca.pem main.py /opt/app/
COPY requirements.txt /tmp

RUN apt update && \
    apt install -y python3 \
    python3-pip \
    cron && \
    rm -rf /var/lib/apt/lists/*


RUN pip3 install -r /tmp/requirements.txt

COPY run_script.cron /etc/cron.d/run_script_cron
RUN chmod 0644 /etc/cron.d/run_script_cron
RUN crontab /etc/cron.d/run_script_cron
RUN touch /var/log/cron.log

CMD cron && tail -f /var/log/cron.log
