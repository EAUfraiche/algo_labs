class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    @classmethod
    def build_tree_from_file(cls, filename):
        """
        Будує дерево з файлу.
        Кожен рядок файлу — рівень дерева.
        Для порожніх вузлів використовуйте 'None'.
        """
        with open(filename, "r") as f:
            lines = [line.strip() for line in f if line.strip()]  

        if not lines:
            return None

        root_val = lines[0]
        if root_val == "None":
            return None

        root = cls(int(root_val))
        queue = [root]

        for level_values in lines[1:]:
            next_level_nodes = []
            level_values = level_values.split()
            idx = 0
            for node in queue:
                if idx < len(level_values):
                    if level_values[idx] != "None":
                        node.left = cls(int(level_values[idx]))
                        next_level_nodes.append(node.left)
                    idx += 1

                if idx < len(level_values):
                    if level_values[idx] != "None":
                        node.right = cls(int(level_values[idx]))
                        next_level_nodes.append(node.right)
                    idx += 1

            queue = next_level_nodes

        return root

    def sum_left_leaves(self):
        total = 0
        if self.left:
            if not self.left.left and not self.left.right:
                total += self.left.value
            else:
                total += self.left.sum_left_leaves()
        if self.right:
            total += self.right.sum_left_leaves()
        return total

    def sum_right_leaves(self):
        total = 0
        if self.right:
            if not self.right.left and not self.right.right:
                total += self.right.value
            else:
                total += self.right.sum_right_leaves()
        if self.left:
            total += self.left.sum_right_leaves()
        return total


filename = "/home/taras/labs/tree_lab32.txt"
root = BinaryTree.build_tree_from_file(filename)
if root:
    print("Сума лівих листків:", root.sum_left_leaves())
    print("Сума правих листків:", root.sum_right_leaves())
else:
    print("Дерево порожнє.")