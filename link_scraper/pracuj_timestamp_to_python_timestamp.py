from datetime import datetime


def cast_pracuj_str_to_datetime(str_datetime: str) -> datetime:
    """
    Pracuj.pl saves dates in format like: 2023-11-08T22:59:59ZZ
    We cast this to python datetime to avoid confusion.
    """
    return datetime.strptime(str_datetime[:-2], "%Y-%m-%dT%H:%M:%S")
