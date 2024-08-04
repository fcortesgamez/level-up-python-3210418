import unittest
from challengues.indexall import index_all


class TestIndexAll(unittest.TestCase):
    def test_index_all_single_occurrence(self):
        search_list = [1, 2, 3, 4, 5]
        item = 3
        expected_result = [[2]]
        self.assertEqual(index_all(search_list, item), expected_result)

    def test_index_all_multiple_occurrences(self):
        search_list = [1, 2, 3, 2, 4, 2, 5]
        item = 2
        expected_result = [[1], [3], [5]]
        self.assertEqual(index_all(search_list, item), expected_result)

    def test_index_all_nested_lists(self):
        search_list = [1, [2, 3], [4, [2, 5]], 6, [2, 7]]
        item = 2
        expected_result = [[1, 0], [2, 1, 0], [4, 0]]
        self.assertEqual(index_all(search_list, item), expected_result)

    def test_index_all_empty_list(self):
        search_list = []
        item = 2
        expected_result = []
        self.assertEqual(index_all(search_list, item), expected_result)

    def test_index_all_no_occurrence(self):
        search_list = [1, 3, 5, 7]
        item = 2
        expected_result = []
        self.assertEqual(index_all(search_list, item), expected_result)


if __name__ == "__main__":
    unittest.main()
