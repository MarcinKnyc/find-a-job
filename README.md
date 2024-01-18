# Job search
## Setup
job_search_qdrant:
1. SETUP REQUIRES YOU TO CREATE A job_search_qdrant\config\local.yaml config out of job_search_qdrant\config\local.template.yaml config!!!
1. Copy set_connection_variables_debug.sh into a new file and set production variables there. Run the new .sh file.
1. Copy .env into a .env.local file in the project's main folder. Replace the values with ones created above.
1. Install pip packages job_search_postgres, job_offer_exporter and job_search_qdrant.
```
pip install -e ./job_search_postgres
pip install -e ./job_offer_exporter
pip install -e ./job_search_qdrant
```
1. Run postgres database and apply migrations
```
source job_search_postgres\set_connection_variables_debug.sh
docker-compose up -d job_search_postgres
cd job_search_postgres
alembic upgrade head
```
1. Run qdrant database and create collection
```
source job_search_qdrant\set_env_vars_local.sh
docker-compose up -d job_search_qdrant
python3 job_search_qdrant\create_job_offer_collection\create_collection.py
```
1. Run continuous link scraper
1. Run contiunuous offer scraper
1. Run streamlit and flask servers after some data has been scraped
1. ???
1. Success! Go make yourself a coffee :)
