import json
import requests
from bs4 import BeautifulSoup
from typing import List

from fix_str_encoding import fix_str_encoding


def extract_all_values_from_json_for_given_key_recursively(
    json_to_search, key_to_search
) -> List[str]:
    """
    Recursively extract list of all values for given key in a json structure.
    """
    found_values = []
    if isinstance(json_to_search, dict):
        for key, value in json_to_search.items():
            if key == key_to_search:
                  found_values.append(value)
            else:
                found_values.extend(
                    extract_all_values_from_json_for_given_key_recursively(
                        value, key_to_search
                    )
                )
    elif isinstance(json_to_search, list):
        for item in json_to_search:
            found_values.extend(
                extract_all_values_from_json_for_given_key_recursively(
                    item, key_to_search
                )
            )
    return found_values


def fetch_values_json_from_one_page(
    url: str,
    html_tag_type_to_find: str,
    html_tag_identifiers: object,
    keys_to_search_in_json: List[str],
) -> dict[str, List[str]]:
    """
    Generic function used in many places.
    Fetches a page. Finds a json using soup. Finds recursively all values of a given key.

    Parameters:
    base_url (str): The base URL of the website.
    page_num (int): The number of the page to fetch links from.

    Returns:
    json_values: dict[str, list[str]]: For every key in keys_to_search_in_json returns a list of its values in the json. 
        The list may be empty but Nones shouldn't happen.
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    script_tag = soup.find(html_tag_type_to_find, html_tag_identifiers)
    if script_tag is None:
        raise Exception(f"No script tag with identifiers {html_tag_identifiers} found")
    
    try:        
        fetched_json = json.loads(script_tag.string)
    except json.JSONDecodeError:
        raise Exception(
            "Extracted data is not of valid JSON format. Maybe html tag identifiers were updated?"
        )
    # uncomment for debug:
    # print(fetched_json)
    # print('--------------------')

    json_values = {}
    for key_to_search_in_json in keys_to_search_in_json:
        json_values[key_to_search_in_json] = extract_all_values_from_json_for_given_key_recursively(
            json_to_search=fetched_json, key_to_search=key_to_search_in_json
        )        
    
    # Polish-specific characters are wrongly encoded in the json fetched from the website.
    for key, list_of_values in json_values.items():
        for i, value in enumerate(list_of_values):
            if value and type(value) == str:
                list_of_values[i] = fix_str_encoding(str_with_broken_encoding=value)


    return json_values
