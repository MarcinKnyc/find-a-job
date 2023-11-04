import time
from typing import Generator, List
from models import Link, Offer
from repositories.offer_repository import insert_offer
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from scrape_one_job_offer import fetch_job_offer_one_page
from datetime import datetime


def fetch_many_job_offers(
    job_offer_links: List[Link],
    timeout_everytime_ms: int,
    timeout_error_ms: int,
    retries_error: int,
    log_txt: str,
    error_txt: str,
) -> Generator[Offer, None, None]:
    """
    Arguments:
    job_offer_links (List[Link]): List of urls to specific job offers.
    timeout_everytime_ms (int): The time to wait between each page fetch.
    timeout_error_ms (int): The time to wait after an error occurs.
    retries_error (int): The number of retries before skipping a page.
    log_txt (str): The name of the file to write log information to.
    error_txt (str): The name of the file to write error information to.

    Yields:
    offers [Offer]:

    Produces errors to error_txt.
    """
    log_txt, error_txt, _ = validate_and_timestamp_output_paths(
        log_txt, error_txt, "debug/files/results"
    )
    with open(log_txt, "a") as error_file:
        error_file.write(
            f"{datetime.now()}Attempting to fetch {len(job_offer_links)} job offers from Pracuj.pl \n"
        )

    for job_offer_link in job_offer_links:
        for retries in range(retries_error):
            try:
                offer = fetch_job_offer_one_page(link=job_offer_link, error_txt=error_txt)
                yield offer

                time.sleep(timeout_everytime_ms / 1000)
                break
            except Exception as e:
                with open(error_txt, "a") as error_file:
                    error_file.write(
                        f"{datetime.now()}Error fetching job offer from page {job_offer_link.link}. This is the {retries} time. Details: {e}\n"
                    )

                time.sleep(timeout_error_ms / 1000)


if __name__ == "__main__":
    import json

    json_data = json.load(open(r"debug\logs\links_sresults_2023-10-24-13-19-54.json"))
    job_offer_links = json_data
    for offer in fetch_many_job_offers(
        job_offer_links=job_offer_links,
        timeout_everytime_ms=100,
        timeout_error_ms=1000,
        retries_error=5,
        log_txt=r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\offers_log",
        error_txt=r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\offers_error",
    ):
        insert_offer(offer)
    print("success")
