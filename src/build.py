from database import Database

def build():
    database = Database()
    connection = database.get_database_connection()
    database.initialize_database(connection)

if __name__ == "__main__":
    build()