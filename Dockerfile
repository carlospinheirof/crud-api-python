FROM python:3.10.8

LABEL author="José Carlos Pinheiro Filho"
ENV PORT=8080
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT python --version
EXPOSE $PORT