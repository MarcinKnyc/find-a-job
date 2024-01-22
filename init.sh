#!/bin/bash

pip install -r ./requirements.txt # requirements.txt should include all requirements for both streamlit and flask apps
pip install -e ./job_search_qdrant/
pip install -e ./job_search_postgres/
pip install -e ./job_offer_exporter/
