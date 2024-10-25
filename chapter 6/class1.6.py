class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_recursively(node.left, data)
        else:  # данные уникальны
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_recursively(node.right, data)

    def search(self, data):
        return self._search_recursively(self.root, data)

    def _search_recursively(self, node, data):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursively(node.left, data)
        else:
            return self._search_recursively(node.right, data)

    def in_order_traversal(self):
        return self._in_order_recursively(self.root)

    def _in_order_recursively(self, node):
        result = []
        if node:
            result.extend(self._in_order_recursively(node.left))
            result.append(node.data)
            result.extend(self._in_order_recursively(node.right))
        return result

    def pre_order_traversal(self):
        return self._pre_order_recursively(self.root)

    def _pre_order_recursively(self, node):
        result = []
        if node:
            result.append(node.data)
            result.extend(self._pre_order_recursively(node.left))
            result.extend(self._pre_order_recursively(node.right))
        return result

    def post_order_traversal(self):
        return self._post_order_recursively(self.root)

    def _post_order_recursively(self, node):
        result = []
        if node:
            result.extend(self._post_order_recursively(node.left))
            result.extend(self._post_order_recursively(node.right))
            result.append(node.data)
        return result


# Пример использования
tree = BinaryTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)

print(tree.search(5))  # Ожидаемый вывод: <__main__.TreeNode object at ...>
print(tree.search(20))  # Ожидаемый вывод: None

print(tree.in_order_traversal())  # Ожидаемый вывод: [5, 10, 15]
print(tree.pre_order_traversal())  # Ожидаемый вывод: [10, 5, 15]
print(tree.post_order_traversal())  # Ожидаемый вывод: [5, 15, 10]