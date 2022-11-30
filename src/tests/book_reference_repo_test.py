import os
import sqlite3
import unittest
from database import Database
from repositories.book_reference_repo import BookReference


class TestBookReference(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.db = Database()
        self.connection = sqlite3.connect(os.path.join(dirname, "testi.db"))
        self.db.initialize_database(self.connection)
        self.book_reference = BookReference()

    def test_add_to_table_adds_data_to_database(self):
        data = ["Test Author", "Test it to the limit", 2022, "TestPublishing", "test22"]
        self.book_reference.add_to_table(self.connection, data)
        self.assertEqual(len(self.book_reference.get_data(self.connection)), 1)