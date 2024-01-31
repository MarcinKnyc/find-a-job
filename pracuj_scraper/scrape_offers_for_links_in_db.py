
import time
from get_session import get_db_session
from repositories_postgres.link_repository import fetch_all_links_without_offers
from repositories_postgres.offer_repository import insert_offer
from tqdm import tqdm
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from scrape_many_job_offers import fetch_many_job_offers
from sqlalchemy.orm.session import Session

def partition(list, size):
    list_of_lists = []
    for i in range(0, len(list), size):
        list_of_lists.append(list[i : i+size])
    return list_of_lists


def scrape_offer_for_every_link_in_db(
    session: Session,
    timeout_everytime_ms: int,
    timeout_error_ms: int,
    retries_error: int,
    log_txt: str,
    error_txt: str,
):
    log_txt, error_txt, _ = validate_and_timestamp_output_paths(
        log_txt, error_txt, "debug/files/results"
    )
    job_offer_links_postgres = fetch_all_links_without_offers(session=session)
    size = 50
    print(f'splitting {len(job_offer_links_postgres)} links without offers in db to groups of {size}. Expected number of batches: {len(job_offer_links_postgres) / size}')
    job_links_partitioned = partition(job_offer_links_postgres, size=size)
    print(f'Created {len(job_links_partitioned)} batches. Downloading offers for their links one by one.')    
    # for links_postgres_batch in (job_links_partitioned):
    for links_postgres_batch in tqdm(job_links_partitioned):
        for offer in fetch_many_job_offers(
            job_offer_links=links_postgres_batch,
            timeout_everytime_ms=timeout_everytime_ms,
            timeout_error_ms=timeout_error_ms,
            retries_error=retries_error,
            log_txt=log_txt,
            error_txt=error_txt,
        ):
            insert_offer(session=session, offer=offer)

if __name__ == '__main__':
    session = get_db_session()
    while True:
        scrape_offer_for_every_link_in_db(
            session=session,
            timeout_everytime_ms=100,
            timeout_error_ms=1000,
            retries_error=5,
            log_txt="./logs/offers_log",
            error_txt="./logs/offers_error",
        )
        time.sleep(3600*11) # 11h
