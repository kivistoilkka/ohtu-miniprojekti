import unittest
from database import Database
from repositories.book_reference_repo import BookReferenceRepo


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(testing_environment=True)
        self.connection = self.db.get_database_connection()
        self.book_reference = BookReferenceRepo

    def test_reset_database_creates_new_tables(self):
        self.db.reset_database()
        cursor = self.connection.cursor()

        data = cursor.execute(
            "SELECT id, author, title, year, publisher, bib_key, tag FROM bookreferences").fetchall()
        self.assertEqual(data, [])

    def test_get_database_connection_returns_connection(self):
        self.assertNotEqual(self.db.get_database_connection, None)
