# Job search
## Setup
job_search_qdrant:
SETUP REQUIRES YOU TO CREATE A LOCAL.YAML config out of LOCAL.TEMPLATE.YAML config!!!
Run databases (postgres and qdrant) with docker-compose up -d
Create postgres tables with sql
Create qdrant collection with job_offer_qdrant/create_job_offer_collection
Run link scraper once in a while
Run offer scraper once in a while
Run streamlit and flask servers when data has been scraped
???
Profit
