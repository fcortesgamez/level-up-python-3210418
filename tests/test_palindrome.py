import unittest
from challengues.palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))


if __name__ == "__main__":
    unittest.main()
