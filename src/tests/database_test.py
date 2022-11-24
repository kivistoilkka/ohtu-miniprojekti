import os
import sqlite3
import unittest
from database import get_database_connection, drop_tables, create_tables, initialize_database
from repositories.book_reference_repo import BookReference

class TestDatabase(unittest.TestCase):
    def setUp(self):
        dirname = os.path.dirname(__file__)
        self.connection = sqlite3.connect(os.path.join(dirname, "testi.db"))
        self.book_reference = BookReference

    def test_initialize_database_creates_new_tables_with_correct_columns(self):
        initialize_database(self.connection)
        cursor = self.connection.cursor()

        data = cursor.execute("SELECT id, author, title, year, publisher, bib_key FROM bookreferences").fetchall()
        self.assertEqual(data, [])

    

