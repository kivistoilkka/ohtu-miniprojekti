import os
import sqlite3
from pathlib import Path


class Database:
    def __init__(self):
        if not Path(f"{os.path.dirname(__file__)}/../data/").exists():
            Path(f"{os.path.dirname(__file__)}/../data/").mkdir()

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

    def get_database_connection(self):
        dirname = os.path.dirname(__file__)
        connection = sqlite3.connect(
            os.path.join(dirname, "..", "data", "testi.db"))
        return connection

    def initialize_database(self, connection):
        self.drop_tables(connection)
        self.create_tables(connection)
