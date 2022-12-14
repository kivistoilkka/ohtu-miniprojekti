import os
import sqlite3
from pathlib import Path


class Database:
    def __init__(self, testing_environment=False):
        path = ""
        dirname = os.path.dirname(__file__)
        if testing_environment:
            path = os.path.join(dirname, "tests", "test.db")
        else:
            if not Path(f"{os.path.dirname(__file__)}/../data/").exists():
                Path(f"{os.path.dirname(__file__)}/../data/").mkdir()
            path = os.path.join(dirname, "..", "data", "references.db")
        self.connection = self._initialize_connection(path)

    def drop_tables(self, connection):
        cursor = connection.cursor()

        cursor.execute("drop table if exists bookreferences")
        cursor.execute("drop table if exists webreferences")

        connection.commit()

    def create_tables(self, connection):
        cursor = connection.cursor()

        cursor.execute('''
            create table bookreferences (
                id integer primary key,
                author text,
                title text,
                year integer,
                publisher text,
                bib_key text unique,
                tag text
            )
        ''')

        cursor.execute('''
            create table webreferences (
                id integer primary key,
                author text,
                title text,
                year integer,
                url text,
                bib_key text unique,
                tag text
            )
        ''')

        connection.commit()

    def _initialize_connection(self, path):
        connection = sqlite3.connect(
            os.path.join(path))
        return connection

    def get_database_connection(self):
        return self.connection

    def reset_database(self):
        self.drop_tables(self.connection)
        self.create_tables(self.connection)

    def get_used_tags_from_database(self):
        cursor = self.connection.cursor()
        data = cursor.execute(
            "SELECT tag FROM bookreferences \
            UNION \
            SELECT tag FROM webreferences"
        ).fetchall()
        return data

    def key_used(self, bib_key) -> str:
        cursor = self.connection.cursor()
        data = cursor.execute(
            "SELECT 'bookreference' FROM bookreferences \
            WHERE bib_key=? \
            UNION \
            SELECT 'webreference' FROM webreferences \
            WHERE bib_key=?", (bib_key, bib_key,)).fetchone()
        return data
