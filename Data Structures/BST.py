"""
The following script implements BST
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class Tree:
    def __init__(self, key):
        self.root = Node(key)

    def insert(self, new_key, node=None):
        if not node:
            node = self.root

        key = node.key

        if not key:
            node.key = Node(new_key)
        elif key < new_key:
            self.insert(new_key, node.right)
        else:
            self.insert(new_key, node.left)

if __name__ == "__main__":
    t = Tree(5)
    t.insert(6)