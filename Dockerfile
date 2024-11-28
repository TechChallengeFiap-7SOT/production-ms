FROM python:3.10

WORKDIR /app

COPY . /app

# RUN sudo apt-get install libpq-dev python3-dev -y

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=run.py

ENV POSTGRES_STRING_CONN="postgresql+psycopg2://postgres:senha-ms@postgres:5432/pedidos?sslmode=disable&connect_timeout=5"

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
