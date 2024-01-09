import requests
from typing import Optional
from get_session import get_db_session
from models import Offer
from repositories_postgres.offer_repository import fetch_n_random_offers, fetch_offer_by_link
from repositories_qdrant.job_offers_pracuj_repository import JobOffersPracujRepository

API_URL = "http://localhost:15000/job_search"
QUERY = "Chcę być dyrektorem dużej firmy i zarabiać gruby hajs"

def query_similar_job_offer(api_url: str, query: str) -> str:
   response = requests.post(
       url=api_url,
       json={
           "text": query
       },
       verify=False)
   return response.text

def extract_offer_field_from_api_response(input_string: str, line_start_string_to_query_for: str = "Obowiązki: ") -> Optional[str]:
   lines = input_string.splitlines()
   for line in lines:
       if line.startswith(line_start_string_to_query_for):
           return line[len(line_start_string_to_query_for):]
   return None

def extract_offer_title_from_api_response(response):
    return response.splitlines()[2]

def test_one_offer(session, offer_query: Offer, field_to_check: str) -> bool:
    func_repository = JobOffersPracujRepository()
    # print(f'query offer_id: {offer_query.id}')
    # print(f'query offer link: {offer_query.link.link}')
    # print(f'query offer title: {offer_query.title}')
    # print(f'query offer description: {func_repository.get_offer_description_str(job_offer=offer_query)}')
    
    response = query_similar_job_offer(API_URL, func_repository.get_offer_description_str(job_offer=offer_query))
    responsibilities = extract_offer_field_from_api_response(response)
    title = extract_offer_title_from_api_response(response)
    link = extract_offer_field_from_api_response(response, line_start_string_to_query_for="The best job offer we found for you is: Link: ")
    offer_found_by_link = fetch_offer_by_link(session=session, offer_link=link)
    # print('------')
    # print(f'response title: {title}')
    # print(responsibilities)
    # print(f'response description: {func_repository.get_offer_description_str(job_offer=offer_query)}')
    # print('------')
    # # print(f'offer_found_by_response_link.title: {offer_found_by_link.title}')
    # # print(f'offer_found_by_response_link.id: {offer_found_by_link.id}')
    # print(f'offer_found_by_response_link.description: {func_repository.get_offer_description_str(job_offer=offer_found_by_link)}')
    # print(offer_found_by_link.responsibilities)
    # print('------')
    # # print(offer_found_by_link.title == title)
    # # print(offer_found_by_link.link.link == link)
    # # print(offer_found_by_link.id == offer_query.id)
    # # print(func_repository.get_offer_description_str(job_offer=offer_query) ==
    # #    func_repository.get_offer_description_str(job_offer=offer_found_by_link))
    # # print('------')
    match field_to_check:
       case 'description':
          return (func_repository.get_offer_description_str(job_offer=offer_query) ==
            func_repository.get_offer_description_str(job_offer=offer_found_by_link))
       case 'title': 
          return offer_query.title == title
       case 'responsibilities':
          return offer_query.responsibilities == responsibilities

def perform_test(
      session, 
      field_to_check: str, 
      n_offers: int
):
    match field_to_check:
        case 'description':
            print(f'''
                Querying {n_offers} offers randomly from db. 
                Generating their descriptions. 
                Using these descriptions as queries to Flask API. 
                Getting the link from API response and fetching the entire offer, generating its description. 
                Test is successful if query job offer description is exactly the same as the result job offer description.''')
        case _:
            print(f'''
                Querying {n_offers} offers randomly from db. 
                Using their {field_to_check} as queries to Flask API. 
                Test is successful if query job offer {field_to_check} is exactly the same as the result job offer {field_to_check}.''')
    
    
    n_random_offers = fetch_n_random_offers(
        session=session,
        n_offers=n_offers
    )
    results = []
    for offer in n_random_offers:
        results.append(test_one_offer(session, offer_query=offer, field_to_check=field_to_check))
    
    # print (results)
    true_count = len([result for result in results if result]) # only true values
    false_count = len([result for result in results if not result]) # only true values
    all_count = true_count + false_count
    if all_count != n_offers:
       raise Exception("Incorrect number of responses provided by test_one_offer")
    print(f'{true_count} test cases passed successfully. {false_count} test cases failed. {all_count} cases total.')

    accuracy = true_count / all_count
    print(f'accuracy: {accuracy}')
    

if __name__ == "__main__":
   session = get_db_session()
   perform_test(
      session=session,
      field_to_check='description',
      n_offers=100,
   )
   perform_test(
      session=session,
      field_to_check='title',
      n_offers=100,
   )
   perform_test(
      session=session,
      field_to_check='responsibilities',
      n_offers=100,
   )
