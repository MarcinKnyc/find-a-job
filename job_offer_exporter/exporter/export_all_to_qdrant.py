
from datetime import datetime
import time
from get_session import get_db_session
from langchain.vectorstores.qdrant import Qdrant
from repositories_postgres.offer_repository import fetch_all_offers_not_exported_to_qdrant
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from sqlalchemy.orm.session import Session
from datetime import datetime

from repositories_qdrant.get_client import get_qdrant_collection_client
from repositories_qdrant.job_offers_pracuj_repository import JobOffersPracujRepository

def partition(list, size):
    for i in range(0, len(list), size):
        yield list[i : i+size]


def export_every_offer_not_yet_in_qdrant(
    postgres_session: Session,
    qdrant_collection_client: Qdrant,
    timeout_everytime_ms: int,
    timeout_error_ms: int,
    retries_error: int,
    log_txt: str,
    error_txt: str,
):
    log_txt, error_txt, _ = validate_and_timestamp_output_paths(
        log_txt, error_txt, "debug/files/results"
    )
    unexported_job_offers_postgres = fetch_all_offers_not_exported_to_qdrant(session=postgres_session)
    job_offers_pracuj_repository_qdrant = JobOffersPracujRepository()
    size = 50
    print(f'splitting {len(unexported_job_offers_postgres)} unexported offers in db to groups of {size}')
    for unexported_job_offer_batch in partition(unexported_job_offers_postgres, size=size):
        with open(log_txt, "a") as log_file:
            log_file.write(
                f"{datetime.now()}Exporting {len(unexported_job_offer_batch)} offers to qdrant from postgres.\n"
            )
        for retry_num in range(retries_error):
            try:
                print(f"Exporting {len(unexported_job_offer_batch)} from postgres to qdrant")
                job_offers_pracuj_repository_qdrant.add_documents(
                    collection_client=qdrant_collection_client,
                    pracuj_job_descriptions=unexported_job_offer_batch
                )
                print(f"Success. Marking {len(unexported_job_offer_batch)} offers as exported_to_qdrant in postgres.")
                for exported_offer in unexported_job_offer_batch:
                    exported_offer.exported_to_qdrant = datetime.now()
                session.commit()
                time.sleep(timeout_everytime_ms / 1000)
                break
            except Exception as e:
                with open(error_txt, "a") as error_file:
                    error_file.write(
                        f"""{datetime.now()}Error exporting job offer batch. This is the {retry_num} time. 
                        Postgres ID's of offers involved: {[offer.id for offer in unexported_job_offer_batch]}. 
                        Details: {e}\n"""
                    )

                time.sleep(timeout_error_ms / 1000)
        

if __name__ == '__main__':
    session = get_db_session()
    qdrant_collection_client = get_qdrant_collection_client()
    while True:
        export_every_offer_not_yet_in_qdrant(
            postgres_session=session,
            qdrant_collection_client=qdrant_collection_client,
            timeout_everytime_ms=10,
            timeout_error_ms=100,
            retries_error=5,
            log_txt="./logs/offers_export_log",
            error_txt="./logs/offers_export_error",
        )
        time.sleep(3600*11) # 11h
