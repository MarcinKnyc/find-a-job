

from typing import List
from tqdm import tqdm
from get_connection import connect_to_db
from add_timestamp_to_log_filenames import validate_and_timestamp_output_paths
from psycopg2._psycopg import connection
from psycopg2 import sql
from datetime import datetime
from offer import Offer

# def insert_offer(offer: Offer, connection: connection):
#     # SQL query
#     cursor = connection.cursor()
#     insert_query = sql.SQL(
#         "INSERT INTO links (link, date_added) VALUES (%s, %s)"
#     )
#     # Execute the query
#     cursor.execute(insert_query, (link, datetime.now().date()))
#     # Commit the transaction
#     connection.commit()
#     # Close the cursor (and connection?)
#     cursor.close()
    

# def fetch_then_save_to_db_offers_fetched_from_links(
#     log_txt: str, error_txt: str, links_to_offers: List[str], connection: connection
# ) -> None:
#     log_txt, error_txt, _ = validate_and_timestamp_output_paths(
#         log_txt, error_txt, "results"
#     )
#     key_to_search_in_json = "offerAbsoluteUri"
#     for link_to_offer in tqdm(links_to_offers):
#         insert_offer(
#             link=link,
#             connection=connection,
#             log_txt=log_txt,
#             error_txt=error_txt
#         )

if __name__ == '__main__':
    conn = connect_to_db()
    