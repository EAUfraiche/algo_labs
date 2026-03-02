import unittest
from lab22 import has_three_sum


class TestThreeSum(unittest.TestCase):

    def test_example_true(self):
        self.assertTrue(has_three_sum([1, 2, 3], 6))

    def test_no_solution(self):
        self.assertFalse(has_three_sum([1, 2, 4, 5], 100))

    def test_large_numbers(self):
        self.assertTrue(has_three_sum([10**9, 10**9, 10**9], 3 * 10**9))

    def test_minimum_n(self):
        self.assertFalse(has_three_sum([1, 1, 1], 10))

    def test_multiple_options(self):
        self.assertTrue(has_three_sum([5, 1, 3, 4, 2], 9))


if __name__ == "__main__":
    unittest.main()