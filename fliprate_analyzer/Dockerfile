FROM python:3.9-slim-buster

COPY . /usr/src/app

WORKDIR /usr/src/app

RUN pip install .

WORKDIR /usr/src/app/files

ENTRYPOINT ["../entrypoint.sh"]
