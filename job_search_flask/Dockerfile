FROM ubuntu
SHELL ["/bin/bash", "-c"]

RUN apt-get update -yqq
RUN apt-get upgrade -yqq
RUN apt-get install python3 wget curl -yqq
RUN apt-get install git -yqq
RUN apt-get install python3-pip -yqq

COPY init.sh .
RUN source init.sh

ENTRYPOINT ["python3"]
CMD ["find-a-job/job_search_flask/src/job_search_flask.py"]