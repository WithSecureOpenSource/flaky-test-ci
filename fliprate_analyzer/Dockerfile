FROM python:3.9-slim-buster

WORKDIR /app

COPY setup.py /setup.py

RUN pip install .

COPY check_flakes.py /check_flakes.py

COPY entrypoint.sh /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
