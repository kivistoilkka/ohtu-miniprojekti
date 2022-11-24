import os 
import sqlite3



def get_database_connection():
    dirname = os.path.dirname(__file__)

    connection = sqlite3.connect(os.path.join(dirname, "..", "data", "testi.db"))
    #connection.row_factory = sqlite3.Row
    return connection



def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        drop table if exists users;
    ''')

    connection.commit()


def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        create table bookreference (
            id integer primary key,
            author text,
            title text,
            year integer,
            publisher text,
            bib_key text
        );
    ''')

    connection.commit()

def get_data(connection):
    cursor = connection.cursor()

    data = cursor.execute('''
        select * from bookreference;
        
    ''').fetchone()

    print(data)


def initialize_database():
    connection = get_database_connection()
    return connection

    #drop_tables(connection)
    #create_tables(connection)


if __name__ == "__main__":
    connection = initialize_database()
    get_data(connection)
