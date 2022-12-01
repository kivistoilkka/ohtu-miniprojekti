from database import Database
from repositories.book_reference_repo import BookReference
from app import App
from reference_reader import ReferenceReader
from ui.ui import UI
from services.reference_service import ReferenceService
from services.input_validator_service import InputValidator


def main():
    db = Database()
    connection = db.get_database_connection()
    db.initialize_database(connection)
    reference_reader = ReferenceReader()
    book_reference_repo = BookReference(connection)
    validator = InputValidator()
    reference_service = ReferenceService(book_reference_repo, validator)
    app = App(connection, book_reference_repo, db, reference_reader)
    ui = UI(app, reference_service)

    ui.run()


if __name__ == "__main__":
    main()
