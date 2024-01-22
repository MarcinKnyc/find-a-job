#!/bin/bash
while true
do
   docker-compose run -d job_search_link_scraper
   docker-compose run -d job_search_offer_scraper
   docker-compose run -d job_search_offer_exporter
   sleep 86400
done
