# Job search
## Setup
There are 2 modes of setting up: local and production. Launching the application locally doesn't require you to set secure passwords and connection strings, while exposing the app to the web should be done only after securing the databases. Every step in the local setup is also a step in production setup. Steps that are unique to production setup have been marked below. Code fragments in this README file that do not adhere to your selected setup type should be commented out.
1. SETUP REQUIRES YOU TO CREATE A job_search_qdrant\config\local.yaml config out of job_search_qdrant\config\local.template.yaml config!!!
1. (production mode only) Copy set_connection_variables_debug.sh into a new file (ex. set_connection_variables_production.sh) and set production variables there. Run the new .sh file.
1. (production mode only) Copy set_env_vars_local.sh into a new file (ex. set_env_vars_production.sh) and set production variables there. Run the new .sh file.
1. Copy .env into a .env.local file in the project's main folder. Replace the values with ones created above.
1. Install pip packages job_search_postgres and job_search_qdrant.
```
pip install -e ./job_search_postgres
pip install -e ./job_search_qdrant
```
1. Run postgres database and apply migrations
```
docker-compose up -d job_search_postgres
source job_search_postgres\set_connection_variables_debug.sh # local mode
source job_search_postgres\set_connection_variables_production.sh # production mode
cd job_search_postgres
alembic upgrade head
```
1. Run qdrant database and create collection
```
docker-compose up -d job_search_qdrant
source job_search_qdrant\set_env_vars_local.sh # local mode
source job_search_qdrant\set_env_vars_production.sh # production mode
python3 job_search_qdrant\create_job_offer_collection\create_collection.py
```
1. (optional) Open a new terminal window, where the connection environment variables have NOT been set. 
1. (optional) You should consider manually running the scrapers on the first launch. Open a new terminal window, where the connection environment variables have NOT been set.
```
docker-compose up job_search_link_scraper && docker-compose up job_search_offer_scraper && docker-compose up job_search_offer_exporter
```
## Running the application
1. Open a new terminal window, where the connection environment variables have NOT been set.
1. Run the application
```
docker-compose up -d 
```
1. ???
1. Success! Go make yourself a coffee :)
