import database as db
from repositories.book_reference_repo import BookReference
from app import App
from reference_reader import ReferenceReader

def main():
    connection = db.get_database_connection()
    app = App(connection, BookReference, db, ReferenceReader)

    app.run()

if __name__ == "__main__":
    main()