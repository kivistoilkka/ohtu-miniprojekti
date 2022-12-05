from database import Database
from repositories.book_reference_repo import BookReference
from app import App
from ui.stub_ui import StubUI
from services.reference_service import ReferenceService
from services.input_validator_service import InputValidator
from services.bibtex_generator_service import BibtexGeneratorService
from ui.reference_reader import ReferenceReader


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

    def add_reference(self, author, title, year, publ, key):
        # keywordilla Add Reference Values voi syöttää tälle metodille
        # halutut parametrit
        self.ui.add_ref([author, title, year, publ, key])

    # def run(self):
    #     # dirname = os.path.dirname(__file__)
    #     # self.db = Database()
    #     # self.connection = sqlite3.connect(
    #     #     os.path.join(dirname, "tests/robot_testi.db"))
    #     # self.db.initialize_database(self.connection)
    #     # self.book_reference = BookReference(self.connection)
    #     # self.reference_service = ReferenceService(self.book_reference, InputValidator())
    #     self.reference_reader = ReferenceReader()
    #     app = App(self.connection, self.book_reference,
    #               self.db, self.reference_reader)
    #     self.ui = StubUI(app, self.reference_service)

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

    def create_database_entry(self, author, title, year, publ, key):
        data = [author, title, year, publ, key]
        self.book_reference.add_to_table(data)

    def reset_database(self):
        self.db.reset_database()

    def view_ref(self):
        self.ui.view_ref()
