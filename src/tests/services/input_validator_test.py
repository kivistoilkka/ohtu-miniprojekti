import unittest
from services.input_validator_service import InputValidator


class TestInputValidator(unittest.TestCase):
    def setUp(self):
        self.validator = InputValidator()

    def test_validator_raises_exception_if_some_of_the_fields_is_empty(self):
        ref_list = ["", "Test it to the limit",
                    2022, "TestPublishing", "test22"]
        self.assertRaises(ValueError, self.validator.validate, ref_list)

    def test_validator_accepts_correct_list(self):
        ref_list = ["Test Author", "Test it to the limit",
                    2022, "TestPublishing", "test22"]
        fixed_list = self.validator.validate(ref_list)
        self.assertEqual(ref_list, fixed_list)
