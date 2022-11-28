import unittest
from services.reference_service import ReferenceService
from entities.reference import Reference

class StubRepo:
    def __init__(self, expected_list):
        self.expected_list = expected_list
    
    def add_to_table(self, list):
        return list == self.expected_list

    def get_data(self):
        return [(1, "Test Author", "Test it to the limit", 2022, "TestPublishing", "test22")]

class TestReferenceService(unittest.TestCase):
    def setUp(self):
        pass

    def test_valid_reference_can_be_added(self):
        repo = StubRepo(["Test Author", "Test it to the limit", 2022, "TestPublishing", "test22"])
        ref_service = ReferenceService(repo)
        result = ref_service.add_reference("Test Author", "Test it to the limit", 2022, "TestPublishing", "test22")
        self.assertTrue(result)

    def test_all_references_from_database_with_one_reference_can_be_fetched(self):
        repo = StubRepo(["Test Author", "Test it to the limit", 2022, "TestPublishing", "test22"])
        ref_service = ReferenceService(repo)
        expected_list = [Reference("Test Author", "Test it to the limit", 2022, "TestPublishing", "test22")]
        result = ref_service.get_all_references()
        self.assertEqual(str(result[0]), str(expected_list[0]))
