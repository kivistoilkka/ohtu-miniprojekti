import pathlib
import unittest

from services.bibtex_generator_service import BibtexGeneratorService
from entities.reference import Reference


class TestBookReference(unittest.TestCase):
    TEST_FILE = pathlib.Path(__file__).parent.parent.parent.parent.joinpath("test.bib")

    def setUp(self):
        self.bibtex_generator = BibtexGeneratorService()

    def test_create_bibtex_file_creates_correct_file(self):
        refs = [Reference("Test Author", "Test it to the limit", 2022, "TestPublishing", "test22")]
        self.bibtex_generator.create_bibtex_file(refs, "test.bib")

        correct_file = """@Book{test22,\n  author     = "Test Author",\n  title      = "Test it to the limit",\n  publisher  = "TestPublishing",\n  year       = 2022\n}\n\n"""

        self.assertEqual(self.TEST_FILE.open().read(), correct_file)