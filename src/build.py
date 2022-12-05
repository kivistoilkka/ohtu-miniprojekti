from database import Database

def build():
    database = Database()
    database.initialize_database()
    print("New database created!")

if __name__ == "__main__":
    build()
