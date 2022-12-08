import unittest
from database import Database
from repositories.book_reference_repo import BookReferenceRepo


class TestBookReference(unittest.TestCase):
    def setUp(self):
        self.db = Database(testing_environment=True)
        self.connection = self.db.get_database_connection()
        self.db.reset_database()
        self.book_reference = BookReferenceRepo(self.db.get_database_connection())

    def test_add_to_table_adds_data_to_database(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22"]
        self.book_reference.add_to_table(data)
        self.assertEqual(len(self.book_reference.get_data()), 1)

    def test_delete_from_table_deletes_data_from_database(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22"]
        self.book_reference.add_to_table(data)
        self.book_reference.delete_from_table(data[-1])
        self.assertEqual(len(self.book_reference.get_data()), 0)

    def test_ref_to_delete_returns_right_ref(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22"]
        self.book_reference.add_to_table(data)
        self.assertEqual(self.book_reference.get_ref_with_key(
            data[-1])[-1], data[-1])
