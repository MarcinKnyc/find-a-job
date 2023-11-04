from typing import List
from psycopg2 import sql
from psycopg2._psycopg import connection
from psycopg2.errors import UniqueViolation
from datetime import datetime

from get_connection import connect_to_db
# ! pip install psycopg2-binary

def insert_link(link: str, connection: connection):
    # SQL query
    cursor = connection.cursor()
    insert_query = sql.SQL(
        "INSERT INTO links (link, date_added) VALUES (%s, %s)"
    )
    # Execute the query
    cursor.execute(insert_query, (link, datetime.now().date()))
    # Commit the transaction
    connection.commit()
    # Close the cursor (and connection?)
    cursor.close()

def insert_list_of_links(log_txt: str, error_txt: str, connection: connection, links: List[str]):
    # Create a cursor object    
    with open(log_txt, "a") as log_file:
        log_file.write(f"{datetime.now()} Inserting {len(links)} links to postgres\n")

    failed_to_insert = 0
    for link in links:
        try:
            insert_link(
                link=link,
                connection=connection
            )
        except UniqueViolation as e:
            connection.rollback()
            with open(error_txt, "a") as error_file:
                error_file.write(
                    f"{datetime.now()} Error pasting link {link} on {datetime.now()}. Link violates Unique Constraint. This is the 1st and last time (retries not implemented). Details: {e}\n"
                )
            failed_to_insert+=1

    with open(log_txt, "a") as log_file:
        log_file.write(f"{datetime.now()} Successfully inserted {len(links)-failed_to_insert} links to postgres. {failed_to_insert} failed.\n")

if __name__ == '__main__':
    conn = connect_to_db()
    insert_list_of_links(
        connection=conn,
        links=[
            'http://brak_adresu.pl',
            'http://jest_adres.pl'
        ],
        log_txt='debug/logs/insert_links_debug_logs.txt',
        error_txt='debug/logs/insert_links_debug_errors.txt'
    )