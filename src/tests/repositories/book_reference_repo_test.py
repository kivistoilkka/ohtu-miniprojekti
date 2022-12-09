import unittest
from database import Database
from repositories.book_reference_repo import BookReferenceRepo


class TestBookReference(unittest.TestCase):
    def setUp(self):
        self.db = Database(testing_environment=True)
        self.connection = self.db.get_database_connection()
        self.db.reset_database()
        self.book_reference = BookReferenceRepo(self.db.get_database_connection())

    def test_add_to_table_adds_data_to_database_without_tag(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22", ""]
        self.book_reference.add_to_table(data)
        self.assertEqual(len(self.book_reference.get_data()), 1)

    def test_add_to_table_adds_data_to_database_with_tag(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22", "test_tag"]
        self.book_reference.add_to_table(data)
        self.assertEqual(len(self.book_reference.get_data()), 1)

    def test_delete_from_table_deletes_data_from_database(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22", ""]
        self.book_reference.add_to_table(data)
        self.book_reference.delete_from_table(data[-2])
        self.assertEqual(len(self.book_reference.get_data()), 0)

    def test_get_reference_returns_right_ref(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22", ""]
        self.book_reference.add_to_table(data)
        self.assertEqual(self.book_reference.get_reference(
            data[-2])[-2], data[-2])

    def test_get_data_by_tag_returns_right_data(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22", "testitagi"]
        self.book_reference.add_to_table(data)
        data = ["TAuthor", "Test it to the limitttttttttt",
                1999, "TestPublishing3", "test32", ""]
        self.book_reference.add_to_table(data)
        self.assertEqual(
            len(self.book_reference.get_data_by_tag("testitagi")), 1)

    def test_get_tags_returns_right_list(self):
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test22", "testitagi"]
        self.book_reference.add_to_table(data)
        data = ["Test Author", "Test it to the limit",
                2022, "TestPublishing", "test222", "testitagi2"]
        self.book_reference.add_to_table(data)
        self.assertEqual(len(self.book_reference.get_tags()), 2)
