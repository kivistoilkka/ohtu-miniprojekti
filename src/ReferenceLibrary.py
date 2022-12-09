import pathlib

from database import Database
from app import App
from ui.stub_ui import StubUI
from services.reference_service import ReferenceService, ReferenceType
from services.input_validator_service import InputValidator
from services.bibtex_generator_service import BibtexGeneratorService
from ui.reference_reader import ReferenceReader
from repositories.book_reference_repo import BookReferenceRepo
from repositories.web_reference_repo import WebReferenceRepo
from entities.book_reference import BookReference


class ReferenceLibrary:
    def __init__(self):
        self.db = Database(testing_environment=True)
        self.book_reference_repo = BookReferenceRepo(self.db.get_database_connection())
        validator = InputValidator()
        self.web_reference_repo = WebReferenceRepo(self.db.get_database_connection())
        self.reference_service = ReferenceService(
            self.book_reference_repo, self.web_reference_repo, validator
        )
        self.reference_reader = ReferenceReader()
        self.bibtex_generator = BibtexGeneratorService()
        app = App(self.db.get_database_connection(), self.reference_service, self.db, self.bibtex_generator)
        self.ui = StubUI(app, self.reference_service)

    def add_reference(self, author, title, year, publ, key, ref_type_str):
        # keywordilla Add Reference Values voi syöttää tälle metodille
        # halutut parametrit
        self.ui.add_ref([author, title, year, publ, key], ref_type_str)

    def data_in_database_length_should_be(self, length):
        # Logiikka tässä on, että voimme tarkistaa, onko tietokannassa nyt haluttu
        # Viite tarkistamalla datan pituuden
        data = self.ui.reference_service.get_all_references()
        data_as_list = data["book_references"] +  data["web_references"]
        if len(data_as_list) != int(length):
            raise AssertionError(
                f"There's something wrong, {len(data)} != {length}")

    def output_should_contain(self, value):
        output = self.ui.outputs.pop(0)

        if not value in output:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(output)}"
            )

    def create_database_entry(self, author, title, year, publ_or_url, key, ref_type_str):
        data = [author, title, year, publ_or_url, key]
        if ref_type_str == "book_reference":
            self.book_reference_repo.add_to_table(data)
        elif ref_type_str == "website_reference":
            self.web_reference_repo.add_to_table(data)

    def reset_database(self):
        self.db.reset_database()

    def view_ref(self, sort_key, order, type_as_str):
        if type_as_str == "book_references":
            type = ReferenceType.Book
        elif type_as_str == "web_references":
            type = ReferenceType.Website
        else:
            raise ValueError("Incorrect reference type")
        self.ui.view_ref(sort_key, order, type)

    def create_bibtex_file(self, author, title, year, publisher, bib_key, filename):
        data = [BookReference(author, title, int(year), publisher, bib_key)]
        self.bibtex_generator.create_bibtex_file(data, filename)

    def data_in_bibtex_file_should_be(self, filename):
        FILE_LOCATION = pathlib.Path(__file__).parent.parent.joinpath(filename)

        content = """@Book{test01,\n  author     = "Testaaja1",\n  title      = "Testikirja1",\n  publisher  = "Unigrafia",\n  year       = 2001\n}\n\n"""

        if not content == FILE_LOCATION.open().read():
            raise AssertionError(
                f"File {content} does not have correct content {FILE_LOCATION.open().read()}"
            )
