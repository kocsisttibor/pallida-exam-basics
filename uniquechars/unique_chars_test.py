import unittest
from unique_chars import unique_characters

class UniqueCharsTestCases(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(unique_characters(""), [])


    def test_one_letter_string(self):
        self.assertEqual(unique_characters("a"), ["a"])


    def test_duplicated_letter(self):
        self.assertEqual(unique_characters("aa"), [])


    def test_duplicated_letter_and_single_letter(self):
        self.assertEqual(unique_characters("aab"), ["b"])

if __name__ == '__main__':
    unittest.main()