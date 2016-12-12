FROM ubuntu:16.04

RUN apt-get update && \
    apt-get install -y tar git curl vim net-tools build-essential && \
    apt-get install -y python python-dev python-distribute python-pip && \
    apt-get install -y uwsgi uwsgi-plugin-python && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY /web-app.ini /etc/uwsgi/apps-enabled/

RUN mkdir /opt/web-app

COPY /app /opt/web-app/app
COPY /requirements.txt /opt/web-app/
COPY /run.py /opt/web-app/

RUN chown www-data:www-data /opt/web-app

RUN pip install -r /opt/web-app/requirements.txt

ENV HOME /opt/web-app
WORKDIR /opt/web-app
