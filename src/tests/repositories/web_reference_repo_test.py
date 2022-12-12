import unittest
from database import Database
from repositories.web_reference_repo import WebReferenceRepo


class TestBookReference(unittest.TestCase):
    def setUp(self):
        self.db = Database(testing_environment=True)
        self.connection = self.db.get_database_connection()
        self.db.reset_database()
        self.web_reference_repo = WebReferenceRepo(self.db.get_database_connection())

    def test_add_to_table_adds_data_to_database_without_tag(self):
        data = ["Test Author", "Test it to the limit",
                2022, "https://www.helsinki.fi/", "test22", ""]
        self.web_reference_repo.add_to_table(data)
        self.assertEqual(len(self.web_reference_repo.get_data()), 1)

    def test_add_to_table_adds_data_to_database_with_tag(self):
        data = ["Test Author", "Test it to the limit",
                2022, "https://www.helsinki.fi/", "test22", "test_tag"]
        self.web_reference_repo.add_to_table(data)
        self.assertEqual(len(self.web_reference_repo.get_data()), 1)

    def test_delete_from_table_deletes_data_from_database(self):
        data = ["Test Author", "Test it to the limit",
                2022, "https://www.helsinki.fi/", "test22", ""]
        self.web_reference_repo.add_to_table(data)
        self.web_reference_repo.delete_from_table(data[-2])
        self.assertEqual(len(self.web_reference_repo.get_data()), 0)

    def test_get_reference_returns_right_ref(self):
        data = ["Test Author", "Test it to the limit",
                2022, "https://www.helsinki.fi/", "test22", ""]
        self.web_reference_repo.add_to_table(data)
        self.assertEqual(self.web_reference_repo.get_reference(data[-2])[-2], data[-2])

    def test_get_data_by_tag_returns_right_data(self):
        data = ["Test Author", "Test it to the limit",
                2022, "https://www.helsinki.fi/", "test22", "testitagi"]
        self.web_reference_repo.add_to_table(data)
        data = ["TAuthor", "Test it to the limitttttttttt",
                1999, "https://www.helsinki.fi/", "test32", ""]
        self.web_reference_repo.add_to_table(data)
        self.assertEqual(len(self.web_reference_repo.get_data_by_tag("testitagi")), 1)
