import os
import sqlite3
import unittest
from database import Database
from repositories.book_reference_repo import BookReference


class TestBookReference(unittest.TestCase):
    def setUp(self):
        self.db = Database(testing_environment=True)
        self.connection = self.db.get_database_connection()
        self.db.reset_database()
        self.book_reference = BookReference(self.db.get_database_connection())

    def test_add_to_table_adds_data_to_database(self):
        data = ["Test Author", "Test it to the limit", 2022, "TestPublishing", "test22"]
        self.book_reference.add_to_table(data)
        self.assertEqual(len(self.book_reference.get_data()), 1)
    