import os
from database import Database
import sqlite3
from repositories.book_reference_repo import BookReference
from app import App
from ui.stub_ui import StubUI
from services.reference_service import ReferenceService
from ui.reference_reader import ReferenceReader


class ReferenceLibrary:
    def __init__(self) -> None:
        pass

    def add_reference(self):
        author = "testi author"
        title = "testi title"
        year = 0000
        publ = "testi publisher"
        key = "abc"
        self.ui.add_ref([author, title, year, publ, key])

    def add_existing_reference(self):
        pass

    def run(self):
        dirname = os.path.dirname(__file__)
        self.db = Database()
        self.connection = sqlite3.connect(
            os.path.join(dirname, "robot_testi.db"))
        self.db.initialize_database(self.connection)
        self.book_reference = BookReference(self.connection)
        self.reference_service = ReferenceService(self.book_reference)
        self.reference_reader = ReferenceReader()
        app = App(self.connection, self.book_reference,
                  self.db, self.reference_reader)
        self.ui = StubUI(app, self.reference_service)
