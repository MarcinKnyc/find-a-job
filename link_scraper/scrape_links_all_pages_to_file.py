import json
from tqdm import tqdm
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from scrape_links_all_pages import fetch_links_from_pages_from_i_to_j


def fetch_then_save_to_file_links_from_pages_from_i_to_j(
    log_txt: str, error_txt: str, results_json: str, i: int, j: int
) -> None:
    log_txt, error_txt, results_json = validate_and_timestamp_output_paths(
        log_txt, error_txt, results_json
    )
    key_to_search_in_json = "offerAbsoluteUri"
    all_fetched_links_so_far = []
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
        all_fetched_links_so_far += list_of_about_69_links
        with open(results_json, "w") as results_file:
            json.dump(all_fetched_links_so_far, results_file)

if __name__ == '__main__':
    fetch_then_save_to_file_links_from_pages_from_i_to_j(
        log_txt = r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\links_log",
        error_txt = r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\links_error",
        results_json = r"H:\Kopia z dysku D\Polsl\sem VII\inzynierka\projekt inzynierski\link_scraper\debug\logs\links_sresults",
        i=2, 
        j=10
    )