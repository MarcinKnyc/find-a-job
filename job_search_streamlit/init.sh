#!/bin/bash

git clone https://github.com/MarcinKnyc/find-a-job.git
cd find-a-job/
pip install -r ./job_search_streamlit/requirements.txt
pip install -e ./job_search_qdrant/
pip install -e ./job_search_postgres/
