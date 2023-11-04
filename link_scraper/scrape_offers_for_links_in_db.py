
from link_scraper.scrape_many_job_offers import fetch_many_job_offers


def aa():
    job_offer_links_postgres = []
    # todo: get all job offer links from db
    # todo: find a postgres db connection driver, preferably alembic / sqlalchemy
    for offer in fetch_many_job_offers(
        job_offer_links=job_offer_links_postgres,
        timeout_everytime_ms=100,
        timeout_error_ms=1000,
        retries_error=5,
        log_txt=r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\offers_log",
        error_txt=r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\offers_error",
    ):
        # print(offer)
        pass
    print("success")