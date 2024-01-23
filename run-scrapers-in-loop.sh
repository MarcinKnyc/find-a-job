#!/bin/bash
while true
do
   echo "Running the containers in 1 hour intervals, then waiting 10h"
   docker-compose run -d job_search_link_scraper
   sleep 3600
   docker-compose run -d job_search_offer_scraper
   sleep 3600
   docker-compose run -d job_search_offer_exporter
   sleep 36000
done
