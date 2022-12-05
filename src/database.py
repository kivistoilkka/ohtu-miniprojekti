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

        cursor.execute('''
            drop table if exists bookreferences;
        ''')

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
                bib_key text unique
            );
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
