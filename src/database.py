import os 
import sqlite3


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists bookreferences;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table bookreferences (
            id integer primary key,
            author text,
            title text,
            year integer,
            publisher text,
            bib_key text
        );
    ''')

    connection.commit()

def get_database_connection():
    dirname = os.path.dirname(__file__)
    connection = sqlite3.connect(os.path.join(dirname, "..", "data", "testi.db"))
    return connection


def initialize_database(connection):
    drop_tables(connection)
    create_tables(connection)
