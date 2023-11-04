import json
import psycopg2
from psycopg2._psycopg import connection

def connect_to_db(config_path: str = './job_search_postgres/src/db_connection_config.json') -> connection:
    # Load database configuration from JSON file
    with open(config_path) as f:
        db_config = json.load(f)

    # Connect to the database
    return psycopg2.connect(
        dbname=db_config['dbname'],
        user=db_config['user'],
        password=db_config['password'],
        host=db_config['host'],
        port=db_config['port']
    )