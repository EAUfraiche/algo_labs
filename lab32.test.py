import unittest
from lab32 import BinaryTree, branchSums


class TestBranchSums(unittest.TestCase):

    def test_example_tree(self):
        root = BinaryTree(3)
        root.left = BinaryTree(9)
        root.right = BinaryTree(20)
        root.right.left = BinaryTree(15)
        root.right.right = BinaryTree(7)

        self.assertEqual(branchSums(root), 24)

    def test_single_node(self):
        root = BinaryTree(5)
        self.assertEqual(branchSums(root), 0)

    def test_no_left_leaves(self):
        root = BinaryTree(1)
        root.right = BinaryTree(2)
        root.right.right = BinaryTree(3)

        self.assertEqual(branchSums(root), 0)

    def test_multiple_left_leaves(self):
        root = BinaryTree(10)
        root.left = BinaryTree(5)
        root.right = BinaryTree(20)

        root.left.left = BinaryTree(3)
        root.left.right = BinaryTree(7)

        root.right.left = BinaryTree(15)

        self.assertEqual(branchSums(root), 18)


if __name__ == "__main__":
    unittest.main()