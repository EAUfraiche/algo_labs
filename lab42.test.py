import unittest
from lab42 import PriorityQueue


class TestPriorityQueue(unittest.TestCase):

    def setUp(self):
        """Створюється нова черга перед кожним тестом"""
        self.pq = PriorityQueue()

    def test_insert_and_peek(self):
        """Перевірка додавання елементів і peek"""
        self.pq.insert("task1", 3)
        self.pq.insert("task2", 5)
        self.pq.insert("task3", 1)

        top = self.pq.peek()
        self.assertEqual(top.value, "task2")
        self.assertEqual(top.priority, 5)

    def test_extract_max(self):
        """Перевірка видалення найбільшого пріоритету"""
        self.pq.insert("A", 1)
        self.pq.insert("B", 10)
        self.pq.insert("C", 5)

        max_node = self.pq.extract_max()

        self.assertEqual(max_node.value, "B")
        self.assertEqual(max_node.priority, 10)

    def test_change_priority_increase(self):
        """Перевірка збільшення пріоритету"""
        self.pq.insert("A", 1)
        self.pq.insert("B", 2)

        self.pq.change_priority("A", 10)

        top = self.pq.peek()
        self.assertEqual(top.value, "A")

    def test_change_priority_decrease(self):
        """Перевірка зменшення пріоритету"""
        self.pq.insert("A", 10)
        self.pq.insert("B", 5)

        self.pq.change_priority("A", 1)

        top = self.pq.peek()
        self.assertEqual(top.value, "B")

    def test_extract_from_empty(self):
        """Перевірка видалення з порожньої черги"""
        self.assertIsNone(self.pq.extract_max())

    def test_peek_empty(self):
        """peek для порожньої черги"""
        self.assertIsNone(self.pq.peek())

    def test_change_priority_not_found(self):
        """зміна пріоритету неіснуючого елемента"""
        self.pq.insert("A", 1)

        result = self.pq.change_priority("X", 10)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()