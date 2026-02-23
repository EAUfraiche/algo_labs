# test_snake_planting.py
import unittest
from lab12 import snake_planting  # імпорт вашої функції з іншого файлу

class TestSnakePlanting(unittest.TestCase):
    def test_5x5(self):
        grid = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [
            1, 2, 3, 4, 5,
            10, 9, 8, 7, 6,
            11, 12, 13, 14, 15,
            20, 19, 18, 17, 16,
            21, 22, 23, 24, 25
        ]
        self.assertEqual(snake_planting(grid), expected)

    def test_2x4(self):
        grid = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(snake_planting(grid), expected)

    def test_6x1(self):
        grid = [
            [1],
            [2],
            [3],
            [4],
            [5],
            [6]
        ]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(snake_planting(grid), expected)

    def test_1x6(self):
        grid = [
            [1, 2, 3, 4, 5, 6]
        ]
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(snake_planting(grid), expected)

if __name__ == "__main__":
    unittest.main()