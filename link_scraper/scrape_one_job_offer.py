from datetime import datetime
from offer import Offer
from scrape_one_page import fetch_values_json_from_one_page


def fetch_job_offer_one_page(
    url: str,
    error_txt: str
) -> Offer:
    # todo: GET LINK POSTGRES_ID BY URL

    KEYS_TO_SEARCH_IN_JSON = [
        "title",
        "hiringOrganization",
        "datePosted",
        "validThrough",
        "addressCountry",
        "addressRegion",
        "addressLocality",
        "postalCode",  # null 32/47 times; does the key exist then?
        "streetAddress",  # null 32/47 times; does the key exist then?
        "employmentType",
        "industry",
        "baseSalary",  # null more often than not. I think key always exists.
        "jobBenefits",  # Job Benefits can be ommitted when creating a job offer. In that case, the key doesn't exist.
        "responsibilities",
        "experienceRequirements",
    ]
    OPTIONAL_KEYS = [
        "postalCode",
        "streetAddress",
        "baseSalary",
        "jobBenefits",
    ]
    values_fetched_json = fetch_values_json_from_one_page(
        url=url,
        html_tag_type_to_find="script",
        html_tag_identifiers={"type": "application/ld+json"},
        keys_to_search_in_json=KEYS_TO_SEARCH_IN_JSON,
    )

    for key_to_search_in_json in KEYS_TO_SEARCH_IN_JSON:
        # Every key should contain exactly one value, except keys in OPTIONAL_KEYS. They may contain no values.
        # If not, then our JSON is not in the format needed by this program.
        # A known problem is that some offer Jsons don't have the key job benefits. We tolerate that; we interpret that
        # as jobBenefits = None. We write  a warning if we detect another key that causes trouble.
        number_of_values_for_this_key = len(values_fetched_json[key_to_search_in_json])
        if number_of_values_for_this_key > 1:
            raise Exception(
                f"Incorrect amount of values found for key {key_to_search_in_json}. Found {number_of_values_for_this_key}, expected 1."
            )
        if number_of_values_for_this_key == 0:
            if key_to_search_in_json not in OPTIONAL_KEYS:
                with open(error_txt, "a") as error_file:
                    error_file.write(
                        f"{datetime.now()} Warning fetching job offer from page {url}. Details: key {key_to_search_in_json} found in offer Json from pracuj.pl, but with no values attached to it. Interpretting that as None.\n"
                    )
            # we append None here so that we can extract it later with values_fetched_json[key_to_search_in_json][0]
            values_fetched_json[key_to_search_in_json].append(None)
    return Offer(
        title=values_fetched_json["title"][0],
        hiringOrganization=values_fetched_json["hiringOrganization"][0],
        datePosted=values_fetched_json["datePosted"][0],
        validThrough=values_fetched_json["validThrough"][0],
        addressCountry=values_fetched_json["addressCountry"][0],
        addressRegion=values_fetched_json["addressRegion"][0],
        addressLocality=values_fetched_json["addressLocality"][0],
        postalCode=values_fetched_json["postalCode"][0],
        streetAddress=values_fetched_json["streetAddress"][0],
        employmentType=values_fetched_json["employmentType"][0],
        industry=values_fetched_json["industry"][0],
        baseSalary=values_fetched_json["baseSalary"][0],
        jobBenefits=values_fetched_json["jobBenefits"][0],
        responsibilities=values_fetched_json["responsibilities"][0],
        experienceRequirements=values_fetched_json["experienceRequirements"][0],
    )
