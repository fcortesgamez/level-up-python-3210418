import unittest
from challengues.sort_words import sort_words


class TestSortWords(unittest.TestCase):
    def test_sort_words(self):
        self.assertEqual(sort_words("banana ORANGE apple"), "apple banana ORANGE")
        self.assertEqual(sort_words("Hello world"), "Hello world")
        self.assertEqual(sort_words("Python is awesome"), "awesome is Python")
        self.assertEqual(sort_words("Keep calm and code on"), "and calm code Keep on")
        self.assertEqual(sort_words("This is a test"), "a is test This")
        self.assertEqual(sort_words("Programming is fun"), "fun is Programming")


if __name__ == "__main__":
    unittest.main()
