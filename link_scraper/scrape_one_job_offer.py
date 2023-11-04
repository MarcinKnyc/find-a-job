from datetime import datetime
from models import Link, Offer
from pracuj_base_salary_json_to_nullable_string import pracuj_base_salary_json_to_str
from pracuj_timestamp_to_python_timestamp import cast_pracuj_str_to_datetime
from scrape_one_page import fetch_values_json_from_one_page


def fetch_job_offer_one_page(
    link: Link,
    error_txt: str
) -> Offer:
    KEYS_TO_SEARCH_IN_JSON = [
        "title",
        "hiringOrganization",
        "datePosted",
        "validThrough",
        "addressCountry",
        "addressRegion",
        "addressLocality", # null 8/250 times. Key doesn't exist in these 8 cases.
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
        "addressLocality",
        "experienceRequirements",
    ]
    values_fetched_json = fetch_values_json_from_one_page(
        url=link.link,
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
                        f"{datetime.now()} Warning fetching job offer from page {link}. Details: key {key_to_search_in_json} found in offer Json from pracuj.pl, but with no values attached to it. Interpretting that as None.\n"
                    )
            # we append None here so that we can extract it later with values_fetched_json[key_to_search_in_json][0]
            values_fetched_json[key_to_search_in_json].append(None)

    base_salary=pracuj_base_salary_json_to_str(values_fetched_json["baseSalary"][0])
    return Offer(
        title=values_fetched_json["title"][0],
        hiring_organization=values_fetched_json["hiringOrganization"][0],
        date_posted=cast_pracuj_str_to_datetime(values_fetched_json["datePosted"][0]),
        valid_through=cast_pracuj_str_to_datetime(values_fetched_json["validThrough"][0]),
        address_country=values_fetched_json["addressCountry"][0],
        address_region=values_fetched_json["addressRegion"][0],
        address_locality=values_fetched_json["addressLocality"][0],
        postal_code=values_fetched_json["postalCode"][0],
        street_address=values_fetched_json["streetAddress"][0],
        employment_type=values_fetched_json["employmentType"][0],
        industry=values_fetched_json["industry"][0],        
        base_salary_min=base_salary.min_value if base_salary is not None else None,
        base_salary_max=base_salary.max_value if base_salary is not None else None,
        base_salary_currency=base_salary.currency if base_salary is not None else None,
        base_salary_unit=base_salary.unit if base_salary is not None else None,
        job_benefits=values_fetched_json["jobBenefits"][0],
        responsibilities=values_fetched_json["responsibilities"][0],
        experience_requirements=values_fetched_json["experienceRequirements"][0],
        link=link
    )
