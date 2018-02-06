FROM python:3.6.4-alpine
MAINTAINER Vitor Mantovani <vtrmantovani@gmail.com>

RUN apk add --no-cache --update bash git openssh mariadb-dev libffi-dev linux-headers alpine-sdk

RUN addgroup infoglobo && adduser -D -h /home/infoglobo -G infoglobo infoglobo

USER infoglobo
RUN mkdir /home/infoglobo/ibc
RUN mkdir /home/infoglobo/logs
ADD wsgi.py /home/infoglobo/
ADD requirements.txt /home/infoglobo/
ADD ibc /home/infoglobo/ibc
ADD manager.py /home/infoglobo/

RUN cd /home/infoglobo && rm -rf /home/infoglobo/.venv && /usr/local/bin/python -m venv .venv \
    && /home/infoglobo/.venv/bin/pip install --upgrade pip
RUN cd /home/infoglobo && /home/infoglobo/.venv/bin/pip install -r requirements.txt

USER root
RUN chown infoglobo.infoglobo /home/infoglobo -R

USER infoglobo
ADD ./dockerfiles/uwsgi.ini /home/infoglobo/

ADD ./dockerfiles/newrelic.ini /home/infoglobo/
ENV NEW_RELIC_CONFIG_FILE=/home/infoglobo/newrelic.ini

EXPOSE 8080
CMD ["/home/infoglobo/.venv/bin/newrelic-admin", "run-program", "/home/infoglobo/.venv/bin/uwsgi", "--ini", "/home/infoglobo/uwsgi.ini"]