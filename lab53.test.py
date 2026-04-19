import unittest
from lab53 import flood_fill_bfs

class TestFloodFillBFS(unittest.TestCase):

    def test_basic_fill(self):
        field = [
            ['A', 'A', 'B'],
            ['A', 'A', 'B'],
            ['B', 'B', 'B']
        ]

        expected = [
            ['C', 'C', 'B'],
            ['C', 'C', 'B'],
            ['B', 'B', 'B']
        ]

        flood_fill_bfs(field, 0, 0, 'A', 'C', 3, 3)
        self.assertEqual(field, expected)

    def test_no_fill_if_different_color(self):
        field = [
            ['A', 'A'],
            ['A', 'A']
        ]

        original = [row[:] for row in field]

        flood_fill_bfs(field, 0, 0, 'B', 'C', 2, 2)
        self.assertEqual(field, original)

    def test_single_cell(self):
        field = [['A']]
        flood_fill_bfs(field, 0, 0, 'A', 'X', 1, 1)
        self.assertEqual(field, [['X']])

    def test_connected_region(self):
        field = [
            ['A', 'A', 'B', 'B'],
            ['A', 'A', 'B', 'B'],
            ['C', 'C', 'B', 'B']
        ]

        expected = [
            ['X', 'X', 'B', 'B'],
            ['X', 'X', 'B', 'B'],
            ['C', 'C', 'B', 'B']
        ]

        flood_fill_bfs(field, 0, 0, 'A', 'X', 3, 4)
        self.assertEqual(field, expected)


if __name__ == "__main__":
    unittest.main()