import unittest
from services.reference_service import ReferenceService

class StubRepo:
    def __init__(self, expected_list):
        self.expected_list = expected_list
    
    def add_to_table(self, list):
        return list == self.expected_list

class TestReferenceService(unittest.TestCase):
    def setUp(self):
        pass
    
    def test_valid_reference_can_be_added(self):
        repo = StubRepo(["Test Author", "Test it to the limit", 2022, "TestPublishing", "test22"])
        ref_service = ReferenceService(repo)
        result = ref_service.add_reference("Test Author", "Test it to the limit", 2022, "TestPublishing", "test22")
        self.assertTrue(result)