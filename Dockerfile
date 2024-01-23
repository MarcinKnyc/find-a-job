# syntax = docker/dockerfile:experimental
FROM ubuntu
SHELL ["/bin/bash", "-c"]
WORKDIR /app
RUN apt-get update -yqq
RUN apt-get upgrade -yqq
RUN apt-get install python3 wget curl -yqq
RUN apt-get install git -yqq
RUN apt-get install python3-pip -yqq

COPY requirements.txt requirements.txt
COPY init.sh init.sh
COPY job_search_postgres job_search_postgres
COPY job_search_qdrant job_search_qdrant
COPY job_offer_exporter job_offer_exporter

# Use pip cache while installing packages
RUN --mount=type=cache,target=/root/.cache/pip source init.sh

COPY job_search_flask job_search_flask
COPY job_search_streamlit job_search_streamlit

ENTRYPOINT [ "echo" ]
CMD [ "override entrypoint in docker-compose.yml" ]
