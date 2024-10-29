# syntax = docker/dockerfile:experimental
FROM ubuntu
SHELL ["/bin/bash", "-c"]
WORKDIR /app
RUN apt-get update -yqq
RUN apt-get upgrade -yqq
RUN apt-get install python3 wget curl -yqq
RUN apt-get install git -yqq
RUN apt-get install python3-pip -yqq
RUN rm /usr/lib/python3.12/EXTERNALLY-MANAGED

COPY job_search_postgres job_search_postgres
COPY pracuj_scraper pracuj_scraper

# Use pip cache while installing packages
RUN source pracuj_scraper/init.sh

ENTRYPOINT [ "echo" ]
CMD [ "override entrypoint in docker-compose.yml" ]
