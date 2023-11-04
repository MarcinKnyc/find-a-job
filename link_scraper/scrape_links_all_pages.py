import json
from typing import Generator, List
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from scrape_links_one_page import fetch_links_from_one_page
import time
from tqdm import tqdm


def fetch_links_from_pages_from_i_to_j(
    page_i: int,
    page_j: int,
    base_url: str,
    timeout_everytime_ms: int,
    timeout_error_ms: int,
    retries_error: int,
    log_txt: str,
    error_txt: str,
    key_to_search_in_json: str
) -> Generator[List[str],None,None]:
    """
    Fetches links from multiple pages of a website.

    Parameters:
    page_i (int): The number of the first page to fetch links from.
    page_j (int): The number of the last page to fetch links from.
    base_url (str): The base URL of the website.
    timeout_everytime_ms (int): The time to wait between each page fetch.
    timeout_error_ms (int): The time to wait after an error occurs.
    retries_error (int): The number of retries before skipping a page.
    log_txt (str): The name of the file to write log information to.
    error_txt (str): The name of the file to write error information to.
    results_json (str): The name of the file to write result information to.
    key_to_search_in_json (str): The key in json file whose values are the job offer links.

    Yields:
    list[str]: A list of links from the current page.
    """
    if page_i >= page_j:
        raise Exception("page_i must be less than page_j")

    for page_num in range(page_i, page_j + 1):
        for retries in range(retries_error):
            try:
                # links and scripts found manually. May be subject to change by original website.
                # Important part, may be updated later.
                links = fetch_links_from_one_page(
                    base_url=base_url,
                    page_num=page_num,
                    html_tag_type_to_find='script',
                    html_tag_identifiers= {'id': '__NEXT_DATA__', 'type': 'application/json'},
                    key_to_search_in_json=key_to_search_in_json
                    )
                # Above returns a dict, here we get to the juicy, juicy
                # list of links to job offers
                links = links[key_to_search_in_json]

                with open(log_txt, "a") as log_file:
                    log_file.write(f"Fetched {len(links)} links from page {page_num}\n")

                yield links

                time.sleep(timeout_everytime_ms / 1000)
                break
            except Exception as e:
                with open(error_txt, "a") as error_file:
                    error_file.write(
                        f"Error fetching links from page {page_num}. This is the {retries} time. Details: {e}\n"
                    )

                time.sleep(timeout_error_ms / 1000)
    
