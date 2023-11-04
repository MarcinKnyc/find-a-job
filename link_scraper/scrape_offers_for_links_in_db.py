
from repositories.link_repository import fetch_all_links
from repositories.offer_repository import insert_offer
from link_scraper.scrape_many_job_offers import fetch_many_job_offers

def partition(list, size):
    for i in range(0, len(list), size):
        yield list[i : i+size]


def scrape_offer_for_every_link_in_db():
    job_offer_links_postgres = fetch_all_links()
    for links_postgres_batch in partition(job_offer_links_postgres, size=50):
        # todo: get all job offer links from db
        # todo: find a postgres db connection driver, preferably alembic / sqlalchemy
        for offer in fetch_many_job_offers(
            job_offer_links=links_postgres_batch,
            timeout_everytime_ms=100,
            timeout_error_ms=1000,
            retries_error=5,
            log_txt=r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\offers_log",
            error_txt=r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\offers_error",
        ):
            insert_offer(offer)
        print("success")