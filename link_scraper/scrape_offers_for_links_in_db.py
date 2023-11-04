
from get_session import get_db_session
from repositories.link_repository import fetch_all_links_without_offers
from repositories.offer_repository import insert_offer
from scrape_many_job_offers import fetch_many_job_offers
from sqlalchemy.orm.session import Session

def partition(list, size):
    for i in range(0, len(list), size):
        yield list[i : i+size]


def scrape_offer_for_every_link_in_db(session: Session):
    job_offer_links_postgres = fetch_all_links_without_offers(session=session)
    size = 50
    print(f'splitting {len(job_offer_links_postgres)} links without offers in db to groups of {size}')
    for links_postgres_batch in partition(job_offer_links_postgres, size=size):
        for offer in fetch_many_job_offers(
            job_offer_links=links_postgres_batch,
            timeout_everytime_ms=100,
            timeout_error_ms=1000,
            retries_error=5,
            log_txt=r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\offers_log",
            error_txt=r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\offers_error",
        ):
            insert_offer(session=session, offer=offer)
        print("success")

if __name__ == '__main__':
    session = get_db_session()
    scrape_offer_for_every_link_in_db(session=session)
