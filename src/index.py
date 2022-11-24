import database as db
from repositories.book_reference_repo import BookReference
from app import App

def main():
    connection = db.get_database_connection()
    app = App(connection, BookReference, db)

    app.run()

if __name__ == "__main__":
    main()