

from tqdm import tqdm
from get_connection import connect_to_db
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from insert_links import insert_list_of_links
from scrape_links_all_pages import fetch_links_from_pages_from_i_to_j
from psycopg2._psycopg import connection

def fetch_then_save_to_db_links_from_pages_from_i_to_j(
    log_txt: str, error_txt: str, i: int, j: int, connection: connection
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
            connection=connection,
            log_txt=log_txt,
            error_txt=error_txt
        )

if __name__ == '__main__':
    conn = connect_to_db()
    fetch_then_save_to_db_links_from_pages_from_i_to_j(
        connection=conn,
        error_txt='iter1\logs\links_error',
        i=2,
        j=1000,
        log_txt='iter1\logs\links_log'
    )