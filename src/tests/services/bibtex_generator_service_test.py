import pathlib
import unittest

from services.bibtex_generator_service import BibtexGeneratorService
from entities.book_reference import BookReference


class TestBookReference(unittest.TestCase):
    TEST_FILE = pathlib.Path(
        __file__).parent.parent.parent.parent.joinpath("test.bib")

    def setUp(self):
        self.bibtex_generator = BibtexGeneratorService()

    def test_create_bibtex_file_creates_correct_file(self):
        refs = {'bookreferences': [BookReference(
            "Yrjänä Änkyräinen", "Test it to the limit", 2022, "TestPublishing", "test22", "")]}
        self.bibtex_generator.create_bibtex_file(refs, "test.bib")

        correct_file = """@Book{test22,\n  author     = "Yrj{\\"a}n{\\"a} {\\"A}nkyr{\\"a}inen",\n  title      = "Test it to the limit",\n  publisher  = "TestPublishing",\n  year       = 2022\n}\n\n"""

        self.assertEqual(self.TEST_FILE.open().read(), correct_file)

    def test_create_bibtex_file_raises_an_exception_if_there_is_no_references(self):
        self.assertRaises(
            ValueError, self.bibtex_generator.create_bibtex_file, [], "test.bib")
