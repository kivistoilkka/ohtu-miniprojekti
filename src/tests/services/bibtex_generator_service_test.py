import pathlib
import unittest

from services.bibtex_generator_service import BibtexGeneratorService
from entities.book_reference import BookReference
from entities.web_reference import WebReference


class TestBookReference(unittest.TestCase):
    TEST_FILE = pathlib.Path(
        __file__).parent.parent.parent.parent.joinpath("test.bib")

    def setUp(self):
        self.bibtex_generator = BibtexGeneratorService()

    def test_create_bibtex_file_creates_correct_file_with_only_book_references(self):
        refs = {'book_references': [BookReference(
            "Yrjänä Änkyräinen", "Test it to the limit", 2022, "TestPublishing", "test22", "")], 'web_references': []}
        self.bibtex_generator.create_bibtex_file(refs, "test.bib")

        correct_file = """@book{test22,\n  author     = "Yrj{\\"a}n{\\"a} {\\"A}nkyr{\\"a}inen",\n  title      = "Test it to the limit",\n  publisher  = "TestPublishing",\n  year       = 2022\n}\n\n"""

        self.assertEqual(self.TEST_FILE.open().read(), correct_file)

    def test_create_bibtex_file_creates_correct_file_with_only_web_references(self):
        refs = {'book_references': [], 'web_references': [WebReference(
            "Beck, Kent et al.", "Manifesto for Agile Software Development", 2001, "http://www.agilemanifesto.org/", "beck2001agile", "")]}
        self.bibtex_generator.create_bibtex_file(refs, "test.bib")

        correct_file = """@misc{beck2001agile,\n  author     = "Beck, Kent et al.",\n  title      = "Manifesto for Agile Software Development",\n  url        = "http://www.agilemanifesto.org/",\n  year       = 2001\n}\n\n"""

        self.assertEqual(self.TEST_FILE.open().read(), correct_file)

    def test_create_bibtex_file_appends_file_type_to_file_name_if_it_is_not_there(self):
        refs = {'book_references': [], 'web_references': [WebReference(
            "Beck, Kent et al.", "Manifesto for Agile Software Development", 2001, "http://www.agilemanifesto.org/", "beck2001agile", "")]}
        self.bibtex_generator.create_bibtex_file(refs, "test")

        correct_file = """@misc{beck2001agile,\n  author     = "Beck, Kent et al.",\n  title      = "Manifesto for Agile Software Development",\n  url        = "http://www.agilemanifesto.org/",\n  year       = 2001\n}\n\n"""

        self.assertEqual(self.TEST_FILE.open().read(), correct_file)

    def test_create_bibtex_file_raises_an_exception_if_there_are_no_references(self):
        with self.assertRaises(ValueError) as cm:
            self.bibtex_generator.create_bibtex_file({"book_references": [], "web_references": []}, "test.bib")
        self.assertEqual(str(cm.exception), "Lisättyjä viitteitä ei ole, joten BibTeX-tiedostoa ei voi luoda!")

    def test_create_bibtex_file_raises_an_exception_if_called_with_other_than_book_or_web_references(self):
        with self.assertRaises(ValueError) as cm:
            self.bibtex_generator.create_bibtex_file({"book_references": [], "article_references": [BookReference(
            "Yrjänä Änkyräinen", "Test it to the limit", 2022, "TestPublishing", "test22", "")], "web_references": []}, "test.bib")
        self.assertEqual(str(cm.exception), "Vain kirja- ja verkkosivuviitteet ovat sallittuja!")
