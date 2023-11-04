from models import Link
from sqlalchemy.orm.session import Session
from typing import List
from psycopg2.errors import UniqueViolation
from datetime import datetime


def fetch_all_links(session: Session) -> list[Link]:
    return session.query(Link).all()


def insert_link(link: Link, session: Session) -> None:
    session.add(link)
    session.commit()


def insert_list_of_links(
    log_txt: str, error_txt: str, session: Session, links: List[str]
):
    # Create a cursor object
    with open(log_txt, "a") as log_file:
        log_file.write(f"{datetime.now()} Inserting {len(links)} links to postgres\n")

    failed_to_insert = 0
    for link_str in links:
        try:
            link = Link(link=link_str, date_added=datetime.now().date())
            insert_link(link=link, session=session)
        except UniqueViolation as e:
            session.rollback()
            with open(error_txt, "a") as error_file:
                error_file.write(
                    f"{datetime.now()} Error pasting link {link_str} on {datetime.now()}. Link violates Unique Constraint. This is the 1st and last time (retries not implemented). Details: {e}\n"
                )
            failed_to_insert += 1
        except Exception as e:
            session.rollback()
            with open(error_txt, "a") as error_file:
                error_file.write(
                    f"{datetime.now()} Error pasting link {link_str} on {datetime.now()}. This is the 1st and last time (retries not implemented). Details: {e}\n"
                )
            failed_to_insert += 1

    with open(log_txt, "a") as log_file:
        log_file.write(
            f"{datetime.now()} Successfully inserted {len(links)-failed_to_insert}/{len(links)} links to postgres. {failed_to_insert} failed.\n"
        )
