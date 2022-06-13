FROM python:3.8.13-buster

#COPY pages /pages
COPY api /api
COPY app.py app.py
COPY TheBurst /TheBurst
COPY image /image
COPY requirements.txt /requirements.txt
COPY .env .env

RUN pip install -U pip
RUN pip install -r requirements.txt

CMD uvicorn api.api_fast:app --host 0.0.0.0
