import pickle
import unittest
from challengues.dictionary import save_dict, load_dict


class TestDictionary(unittest.TestCase):
    def test_save_dict(self):
        file_path = "tests/data/test_save_dict"
        test_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

        save_dict(test_dict, file_path)

        with open(file_path, "rb") as f:
            content = pickle.load(f)

        expected_content = {"key1": "value1", "key2": "value2", "key3": "value3"}
        self.assertEqual(content, expected_content)

    def test_load_dict(self):
        file_path = "tests/data/test_load_dict"
        expected_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}

        loaded_dict = load_dict(file_path)

        self.assertEqual(loaded_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
