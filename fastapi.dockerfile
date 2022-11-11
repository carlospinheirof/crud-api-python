FROM python:3.10.8

LABEL author="José Carlos Pinheiro Filho"
ENV PORT=8000
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE $PORT
