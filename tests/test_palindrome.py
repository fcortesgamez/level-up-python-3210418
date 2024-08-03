import unittest
from challengues.palindrome import is_palindrome, only_letters


class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("A man, a plan, a canal: Panama"))
        self.assertFalse(is_palindrome("hello"))
        self.assertFalse(is_palindrome("python"))

    def test_only_letters(self):
        self.assertEqual(list(only_letters("Hello123")), ["H", "e", "l", "l", "o"])
        self.assertEqual(list(only_letters("12345")), [])
        self.assertEqual(
            list(only_letters("Hello, World!")),
            ["H", "e", "l", "l", "o", "W", "o", "r", "l", "d"],
        )


if __name__ == "__main__":
    unittest.main()
