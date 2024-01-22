import requests
from bs4 import BeautifulSoup

def fetch_number_of_link_pages(url: str = 'https://www.pracuj.pl/praca') -> int:
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    tag = soup.find('span', {'data-test': 'top-pagination-max-page-number'})

    # Extract the value of the tag
    value = tag.text if tag else None

    return int(value)

if __name__ == '__main__':
    print(fetch_number_of_link_pages())