import unittest

from challengues.factor import get_prime_factors


class TestGetPrimeFactors(unittest.TestCase):
    def test_get_prime_factors(self):
        self.assertEqual(get_prime_factors(15), [3, 5])
        self.assertEqual(get_prime_factors(45), [3, 3, 5])
        self.assertEqual(get_prime_factors(130), [2, 5, 13])
        self.assertEqual(get_prime_factors(630), [2, 3, 3, 5, 7])
        self.assertEqual(get_prime_factors(780), [2, 2, 3, 5, 13])


if __name__ == "__main__":
    unittest.main()
