FROM python:3.9-slim-buster

RUN pip install pandas

COPY check_flakes.py /check_flakes.py

ENTRYPOINT ["python","check_flakes.py"]
