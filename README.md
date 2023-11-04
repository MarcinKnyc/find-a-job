# Job search
## Setup
job_search_qdrant:
SETUP REQUIRES YOU TO CREATE A LOCAL.YAML config out of LOCAL.TEMPLATE.YAML config!!!
1. Run databases (postgres and qdrant) with docker-compose up -d
1. Create postgres tables with sql
1. Create qdrant collection with job_offer_qdrant/create_job_offer_collection
1. Run link scraper once in a while
1. Run offer scraper once in a while
1. Run streamlit and flask servers when data has been scraped
1. ???
1. Profit
