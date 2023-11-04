from typing import List
from psycopg2 import sql
from psycopg2._psycopg import connection
from datetime import datetime
from get_connection import connect_to_db

# from get_connection import connect_to_db
# ! pip install psycopg2-binary

def insert_link(link: str, cursor):
    # SQL query
    insert_query = sql.SQL(
        "INSERT INTO links (link, date_added) VALUES (%s, %s)"
    )
    # Execute the query
    cursor.execute(insert_query, (link, datetime.now().date()))

def insert_list_of_links(conn: connection, links: List[str]):
    # Create a cursor object
    cursor = conn.cursor()

    for link in links:
        insert_link(
            link=link,
            cursor=cursor
        )

    # Commit the transaction
    conn.commit()
    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == '__main__':
    conn = connect_to_db()
    insert_list_of_links(
        conn=conn,
        links=[
            'http://brak_adresu.pl',
            'http://jest_adres.pl'
        ]
    )