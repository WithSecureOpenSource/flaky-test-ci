FROM python:3.9-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install .

ENTRYPOINT ["./entrypoint.sh"]
