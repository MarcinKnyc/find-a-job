FROM ubuntu

RUN apt-get update -yqq
RUN apt-get upgrade -yqq
RUN apt-get install python3 wget curl -yqq
RUN apt-get install python3-pip -yqq

RUN mkdir model
COPY requirements.txt .

RUN pip install -r requirements.txt
COPY src src

ENTRYPOINT ["python3"]
CMD ["src/job_search_flask.py"]