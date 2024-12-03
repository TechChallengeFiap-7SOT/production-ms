FROM --platform=linux/amd64 python:3.10 AS build

WORKDIR /app

COPY . /app

# RUN sudo apt-get install libpq-dev python3-dev -y

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=run.py

ENV POSTGRES_STRING_CONN="postgresql+psycopg2://postgres:senha123@pedidos.cc1t1ip1k3ol.us-east-1.rds.amazonaws.com:5432/postgres"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
