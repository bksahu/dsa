"""
Given a binary tree, connect each node with its level order successor. The last node of each level should point to the first node of the next level.
"""

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_tree(self):
        print("Travel using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next

def connect_all_siblings(root):
    if not root: return root 
    q = deque([root])

    prev_node = None
    while q:
        for _ in range(len(q)):
            curr_node = q.popleft()

            if prev_node:
                prev_node.next = curr_node
            prev_node = curr_node

            if curr_node.left: q.append(curr_node.left)
            if curr_node.right: q.append(curr_node.right)

    return root

if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_all_siblings(root)
    root.print_tree()