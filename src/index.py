from database import Database
from repositories.book_reference_repo import BookReference
from app import App
from reference_reader import ReferenceReader

def main():
    db = Database()
    connection = db.get_database_connection()
    reference_reader = ReferenceReader()
    book_reference_repo = BookReference()
    app = App(connection, book_reference_repo, db, reference_reader)

    app.run()

if __name__ == "__main__":
    main()