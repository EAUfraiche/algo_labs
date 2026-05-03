import unittest
import os
from lab7 import read_matrix, prim_mst


class TestMST(unittest.TestCase):

    def setUp(self):
        self.test_file = "test_islands.csv"
        with open(self.test_file, "w") as f:
            f.write("0,2,3\n")
            f.write("2,0,1\n")
            f.write("3,1,0\n")

    def tearDown(self):
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_read_matrix(self):
        matrix = read_matrix(self.test_file)
        expected = [
            [0.0, 2.0, 3.0],
            [2.0, 0.0, 1.0],
            [3.0, 1.0, 0.0]
        ]
        self.assertEqual(matrix, expected)

    def test_prim_mst_small(self):
        matrix = [
            [0, 2, 3],
            [2, 0, 1],
            [3, 1, 0]
        ]
        self.assertEqual(prim_mst(matrix), 3)

    def test_prim_mst_single_node(self):
        matrix = [[0]]
        self.assertEqual(prim_mst(matrix), 0)

    def test_prim_mst_line(self):
        matrix = [
            [0, 5, 0],
            [5, 0, 7],
            [0, 7, 0]
        ]
        self.assertEqual(prim_mst(matrix), 12)

    def test_prim_mst_disconnected(self):
        matrix = [
            [0, 1, 0],
            [1, 0, 0],
            [0, 0, 0]
        ]
        result = prim_mst(matrix)
        self.assertTrue(result >= 1)


if __name__ == "__main__":
    unittest.main()