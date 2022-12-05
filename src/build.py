from database import Database

def build():
    database = Database()
    database.initialize_database()

if __name__ == "__main__":
    build()