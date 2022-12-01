import os
from database import Database
import sqlite3
from repositories.book_reference_repo import BookReference
from app import App
from ui.stub_ui import StubUI
from services.reference_service import ReferenceService
from reference_reader import ReferenceReader
from services.input_validator_service import InputValidator



class ReferenceLibrary:
    def __init__(self) -> None:
        pass

    def add_reference(self, author, title, year, publ, key):
        #keywordilla Add Reference Values voi syöttää tälle metodille
        #halutut parametrit
        self.ui.add_ref([author, title, year, publ, key])


    def run(self):
        dirname = os.path.dirname(__file__)
        self.db = Database()
        self.connection = sqlite3.connect(
            os.path.join(dirname, "tests/robot_testi.db"))
        self.db.initialize_database(self.connection)
        self.book_reference = BookReference(self.connection)
        self.reference_service = ReferenceService(self.book_reference, InputValidator())
        self.reference_reader = ReferenceReader()
        app = App(self.connection, self.book_reference,
                  self.db, self.reference_reader)
        self.ui = StubUI(app, self.reference_service)

    def data_in_database_length_should_be(self, length):
        #Logiikka tässä on, että voimme tarkistaa, onko tietokannassa nyt haluttu
        #Viite tarkistamalla datan pituuden
        data = self.ui.reference_service.get_all_references()
        if len(data) != int(length):
            raise AssertionError(
                f"There's something wrong, {len(data)} != {length}")