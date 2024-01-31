

import time
from get_session import get_db_session
from fetch_number_of_link_pages import fetch_number_of_link_pages
from repositories_postgres.link_repository import insert_list_of_links
from tqdm import tqdm
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from scrape_links_all_pages import fetch_links_from_pages_from_i_to_j
from psycopg2._psycopg import connection
from sqlalchemy.orm.session import Session

def fetch_then_save_to_db_links_from_pages_from_i_to_j(
    log_txt: str, error_txt: str, i: int, j: int, session: Session
) -> None:
    log_txt, error_txt, _ = validate_and_timestamp_output_paths(
        log_txt, error_txt, "results"
    )
    key_to_search_in_json = "offerAbsoluteUri"
    for list_of_about_69_links in tqdm(fetch_links_from_pages_from_i_to_j(
        page_i = i,
        page_j = j,
        base_url = 'https://www.pracuj.pl/praca',
        timeout_everytime_ms = 100,
        timeout_error_ms = 1000,
        retries_error = 5,
        log_txt = log_txt,
        error_txt = error_txt,
        key_to_search_in_json = key_to_search_in_json
    )):
        insert_list_of_links(
            links=list_of_about_69_links,
            session=session,
            log_txt=log_txt,
            error_txt=error_txt
        )

if __name__ == '__main__':
    session=get_db_session()
    while True:
        number_of_link_pages = fetch_number_of_link_pages()
        fetch_then_save_to_db_links_from_pages_from_i_to_j(
            session=session,
            error_txt='./logs/links_error',
            i=2, # start at page 2. page 1 doesn't work, because it has a different url.
            j=number_of_link_pages,
            log_txt='./logs/links_log'
        )
        time.sleep(3600*11) # 11h