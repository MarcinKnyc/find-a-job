FROM ubuntu
SHELL ["/bin/bash", "-c"]

RUN apt-get update -yqq
RUN apt-get upgrade -yqq
RUN apt-get install python3 wget curl -yqq
RUN apt-get install git -yqq
RUN apt-get install python3-pip -yqq

COPY init.sh .
RUN source init.sh

ENTRYPOINT ["streamlit", "run", "find-a-job/job_search_postgres/src/job_search_streamlit.py", "--server.port=18503"]