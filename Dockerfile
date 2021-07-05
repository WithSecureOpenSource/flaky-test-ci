FROM python:3.9-slim-buster

WORKDIR /app

RUN pip install pandas junitparser

COPY check_flakes.py /check_flakes.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
