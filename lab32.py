class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    if root is None:
        return 0

    sum_left = 0

    if root.left and root.left.left is None and root.left.right is None:
        sum_left += root.left.value

    sum_left += branchSums(root.left)
    sum_left += branchSums(root.right)

    return sum_left


def build_tree():
    value = input("Введіть значення кореня (або None): ")
    if value == "None":
        return None

    root = BinaryTree(int(value))
    queue = [root]

    while queue:
        node = queue.pop(0)

        left = input(f"Лівий нащадок для {node.value} (або None): ")
        if left != "None":
            node.left = BinaryTree(int(left))
            queue.append(node.left)

        right = input(f"Правий нащадок для {node.value} (або None): ")
        if right != "None":
            node.right = BinaryTree(int(right))
            queue.append(node.right)

    return root


root = build_tree()

result = branchSums(root)
print("Сума лівих листків:", result)