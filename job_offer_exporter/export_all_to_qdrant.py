
from datetime import datetime
import time
from get_session import get_db_session
from repositories.offer_repository import fetch_all_offers_not_exported_to_qdrant
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from sqlalchemy.orm.session import Session

def partition(list, size):
    for i in range(0, len(list), size):
        yield list[i : i+size]


def export_every_offer_not_yet_in_qdrant(
    session: Session,
    timeout_everytime_ms: int,
    timeout_error_ms: int,
    retries_error: int,
    log_txt: str,
    error_txt: str,
    model_name: str,
):
    log_txt, error_txt, _ = validate_and_timestamp_output_paths(
        log_txt, error_txt, "debug/files/results"
    )
    unexported_job_offers_postgres = fetch_all_offers_not_exported_to_qdrant(session=session)
    size = 50
    print(f'splitting {len(unexported_job_offers_postgres)} unexported offers in db to groups of {size}')
    for unexported_job_offer_batch in partition(unexported_job_offers_postgres, size=size):
        with open(log_txt, "a") as error_file:
            log_txt.write(
                f"{datetime.now()}Exporting {len(unexported_job_offer_batch)} offers to qdrant from postgres.\n"
            )
        for unexported_job_offer in unexported_job_offer_batch:
            for retry_num in range(retries_error):
                try:
                    # vectorize_long_string(offer, model=model_name)
                    # export_offer(session=session, offer=offer)
                    time.sleep(timeout_everytime_ms / 1000)
                    break
                except Exception as e:
                    with open(error_txt, "a") as error_file:
                        error_file.write(
                            f"{datetime.now()}Error exporting job offer. This is the {retry_num} time. Details: {e}\n"
                        )

                    time.sleep(timeout_error_ms / 1000)
        

if __name__ == '__main__':
    session = get_db_session()
    export_every_offer_not_yet_in_qdrant(
        session=session,
        timeout_everytime_ms=100,
        timeout_error_ms=1000,
        retries_error=5,
        log_txt=r".\iter1\logs\offers_log",
        error_txt=r".\iter1\logs\offers_error",
    )
