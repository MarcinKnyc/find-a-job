from typing import List
from scrape_one_page import fetch_values_json_from_one_page


def fetch_links_from_one_page(
    base_url: str,
    page_num: int,
    html_tag_type_to_find: str,
    html_tag_identifiers: str,
    key_to_search_in_json: str,
) -> dict[str, List[str]]:
    """
    Interface for using fetch_values_json_from_one_page to fetch links from Pracuj.pl.
    It returns a dict with one key, key_to_search_in_json. 
    The value of this key is a List[str] of all links to job offers on this one page.
    """
    return fetch_values_json_from_one_page(
        url=f"{base_url}?pn={page_num}",
        html_tag_type_to_find=html_tag_type_to_find,
        html_tag_identifiers=html_tag_identifiers,
        keys_to_search_in_json=[key_to_search_in_json],
    )
