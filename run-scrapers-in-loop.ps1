while ($true) {
    docker-compose up -d job_search_link_scraper
    Start-Sleep -Seconds 3600
    docker-compose up -d job_search_offer_scraper
    Start-Sleep -Seconds 3600
    docker-compose up -d job_search_offer_exporter
    Start-Sleep -Seconds 36000
}