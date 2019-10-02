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

    def getRoot(self):
        return self.root

    def insert(self, key, node):
        if self.root is None:
            self.root = Node(key)

        if node.key < key:
            if node.right is None:
                node.right = Node(key)
            else:
                self.insert(key, node.right)
        else:
            if node.left is None:
                node.left = Node(key)
            else:
                self.insert(key, node.left)

    def inorderPrint(self, node):
        if node.left:
            self.inorderPrint(node.left)

        print(node.key)

        if node.right:
            self.inorderPrint(node.right)

    @staticmethod
    def minInorder(node):
        node = node.right

        while node.left is not None:
            node = node.left

        return node

    def delete(self, key, node):
        if node is None:
            return node

        if node.key < key:
            node.right = self.delete(key, node.right)
        elif node.key > key:
            node.left = self.delete(key, node.left)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self.minInorder(node)
            node.key = temp.key
            node.right = self.delete(node.key, node.right)


        return node

if __name__ == "__main__":
    t = Tree(5)
    t.insert(4, t.getRoot())
    t.insert(2, t.getRoot())
    t.insert(1, t.getRoot())
    t.insert(3, t.getRoot())
    t.insert(6, t.getRoot())
    t.insert(7, t.getRoot())
    t.insert(6.5, t.getRoot())
    t.insert(8, t.getRoot())
    t.inorderPrint(t.getRoot())
    print("Deleting..")
    t.delete(6, t.getRoot())
    t.inorderPrint(t.getRoot())