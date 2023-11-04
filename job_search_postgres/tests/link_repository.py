from get_session import get_db_session
from repositories.link_repository import insert_list_of_links


if __name__ == '__main__':
    session = get_db_session()
    insert_list_of_links(
        session=session,
        links=[
            'http://brak_adresu.pl',
            'http://jest_adres.pl'
        ],
        log_txt='debug/logs/insert_links_debug_logs.txt',
        error_txt='debug/logs/insert_links_debug_errors.txt'
    )