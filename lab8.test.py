import unittest
import os

from lab8 import solve


class TestIJones(unittest.TestCase):

    def run_test(self, input_data, expected_output):
        with open('ijones.in', 'w') as f:
            f.write(input_data)

        solve()

        with open('ijones.out', 'r') as f:
            result = f.read().strip()

        self.assertEqual(result, str(expected_output))

    def test_single_cell(self):
        self.run_test(
            "1 1\na\n",
            1
        )

    def test_single_row(self):
        self.run_test(
            "4 1\nabcd\n",
            1
        )

    def test_same_letters(self):
        self.run_test(
            "2 2\naa\naa\n",
            4
        )

    def test_different_letters(self):
        self.run_test(
            "2 2\nab\ncd\n",
            4
        )

    def test_mixed_case(self):
        self.run_test(
            "3 2\naba\nbab\n",
            12
        )



if __name__ == "__main__":
    unittest.main()