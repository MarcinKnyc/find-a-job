while ($true) {
    docker-compose run -d job_search_link_scraper
    docker-compose run -d job_search_offer_scraper
    docker-compose run -d job_search_offer_exporter
    Start-Sleep -Seconds 86400
}