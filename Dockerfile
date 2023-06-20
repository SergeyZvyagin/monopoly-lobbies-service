FROM python:3.9-slim

WORKDIR /app

COPY ./ ./

RUN pip install -r requirements.txt
CMD python bin/monopoly-lobbies-service.py -c etc/monopoly-lobbies-service-conf.toml
