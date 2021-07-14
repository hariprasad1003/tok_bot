FROM python:3.6-slim-stretch

WORKDIR /app

COPY . /app

RUN python3 -m pip install -U -r requirements.txt

EXPOSE 8081

CMD ["python3", "main.py"]