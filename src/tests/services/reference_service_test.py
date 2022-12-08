import unittest
from services.book_reference_service import BookReferenceService
from entities.book_reference import BookReference


class StubRepo:
    def __init__(self, expected_data, database_content):
        self.expected_data = expected_data
        self.database_content = database_content

    def add_to_table(self, data):
        self.database_content.append(data)
        return data == self.expected_data

    def get_data(self):
        return self.database_content


class StubValidator:
    def __init__(self):
        pass

    def validate(self, reference_list):
        return reference_list


class TestReferenceService(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_reference_can_be_added(self):
        repo = StubRepo(["Test Author", "Test it to the limit",
                        2022, "TestPublishing", "test22"], [])
        validator = StubValidator()
        ref_service = BookReferenceService(repo, validator)
        result = ref_service.add_reference(
            ["Test Author", "Test it to the limit", 2022, "TestPublishing", "test22"])
        self.assertTrue(result)
        self.assertEqual(len(repo.database_content), 1)

    def test_all_references_from_database_with_one_reference_can_be_fetched(self):
        repo = StubRepo([], [
            (1, "Test Author", "Test it to the limit",
             2022, "TestPublishing", "test22")
        ])
        validator = StubValidator()
        ref_service = BookReferenceService(repo, validator)
        expected_list = [BookReference(
            "Test Author", "Test it to the limit", 2022, "TestPublishing", "test22")]
        result = ref_service.get_all_references()
        self.assertEqual(str(result[0]), str(expected_list[0]))

    def test_all_references_from_database_with_two_references_can_be_fetched(self):
        repo = StubRepo([], [
            (1, "Test Author", "Test it to the limit",
             2022, "TestPublishing", "test22"),
            (2, "Stanley", "This is a story about a man named Stanley",
             2013, "GC", "stan13")
        ])
        validator = StubValidator()
        ref_service = BookReferenceService(repo, validator)
        expected_list = [
            BookReference("Test Author", "Test it to the limit",
                      2022, "TestPublishing", "test22"),
            BookReference(
                "Stanley", "This is a story about a man named Stanley", 2013, "GC", "stan13")
        ]
        result = ref_service.get_all_references()
        for i, ref in enumerate(result):
            self.assertEqual(str(ref), str(expected_list[i]))
