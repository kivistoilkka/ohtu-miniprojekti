import pathlib

from database import Database
from repositories.book_reference_repo import BookReference
from app import App
from ui.stub_ui import StubUI
from services.reference_service import ReferenceService
from services.input_validator_service import InputValidator
from services.bibtex_generator_service import BibtexGeneratorService
from ui.reference_reader import ReferenceReader
from entities.reference import Reference


class ReferenceLibrary:
    def __init__(self):
        self.db = Database(testing_environment=True)
        self.book_reference = BookReference(self.db.get_database_connection())
        validator = InputValidator()
        self.reference_service = ReferenceService(
            self.book_reference, validator)
        self.reference_reader = ReferenceReader()
        self.bibtex_generator = BibtexGeneratorService()
        app = App(self.db.get_database_connection(), self.book_reference,
                  self.db, self.reference_reader, self.bibtex_generator)
        self.ui = StubUI(app, self.reference_service)

    def add_reference(self, author, title, year, publ, key, tag):
        # keywordilla Add Reference Values voi syöttää tälle metodille
        # halutut parametrit
        self.ui.add_ref([author, title, year, publ, key, tag])

    def data_in_database_length_should_be(self, length):
        # Logiikka tässä on, että voimme tarkistaa, onko tietokannassa nyt haluttu
        # Viite tarkistamalla datan pituuden
        data = self.ui.reference_service.get_all_references()
        if len(data) != int(length):
            raise AssertionError(
                f"There's something wrong, {len(data)} != {length}")

    def output_should_contain(self, value):
        output = self.ui.outputs.pop(0)

        if not value in output:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(output)}"
            )

    def create_database_entry(self, author, title, year, publ, key, tag):
        data = [author, title, year, publ, key, tag]
        self.book_reference.add_to_table(data)

    def reset_database(self):
        self.db.reset_database()

    def view_ref(self, sort_key, order):
        self.ui.view_ref(sort_key, order)

    def create_bibtex_file(self, author, title, year, publisher, bib_key, tag, filename):
        data = [Reference(author, title, int(year), publisher, bib_key, tag)]
        self.bibtex_generator.create_bibtex_file(data, filename)

    def data_in_bibtex_file_should_be(self, filename):
        FILE_LOCATION = pathlib.Path(__file__).parent.parent.joinpath(filename)

        content = """@Book{test01,\n  author     = "Testaaja1",\n  title      = "Testikirja1",\n  publisher  = "Unigrafia",\n  year       = 2001\n}\n\n"""

        if not content == FILE_LOCATION.open().read():
            raise AssertionError(
                f"File {content} does not have correct content {FILE_LOCATION.open().read()}"
            )
