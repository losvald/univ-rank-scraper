"""Common code that is likely to be reused if another data source
(and the appropriate scraper) is added.
"""

import os.path
import sqlite3
from contextlib import contextmanager

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "db.sqlite")


@contextmanager
def connect_db(dry_run):
    db = sqlite3.connect(":memory:" if dry_run else DB_PATH)
    _create_schema(db)
    yield db
    db.close()


def _create_schema(db):
    db.execute("""CREATE TABLE IF NOT EXISTS rankings (
    contest NOT NULL,
    year INTEGER NOT NULL,
    rank INTEGER NOT NULL,
    univ NOT NULL,
    score INTEGER NOT NULL,
    penalty INTEGER,
    PRIMARY KEY (contest, year, univ)
    )""")
