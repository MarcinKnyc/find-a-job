import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def get_postgres_url_from_env_variables():
    FIND_A_JOB_USER = os.environ["FIND_A_JOB_USER"]
    FIND_A_JOB_PASSWORD = os.environ["FIND_A_JOB_PASSWORD"]
    FIND_A_JOB_HOST = os.environ["FIND_A_JOB_HOST"]
    FIND_A_JOB_PORT = os.environ["FIND_A_JOB_PORT"]
    FIND_A_JOB_DBNAME = os.environ["FIND_A_JOB_DBNAME"]
    url = f"postgresql://{FIND_A_JOB_USER}:{FIND_A_JOB_PASSWORD}@{FIND_A_JOB_HOST}:{FIND_A_JOB_PORT}/{FIND_A_JOB_DBNAME}"
    return url


def get_db_session():
    engine = create_engine(url=get_postgres_url_from_env_variables())
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
