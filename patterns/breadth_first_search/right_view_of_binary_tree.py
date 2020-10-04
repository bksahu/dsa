"""
Given a binary tree, return an array containing nodes in its right view. The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
"""

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def tree_right_view(root):
    result = []
    if not root: return result
    q = deque([root])

    while q:
        if q: result.append(q[-1])
        for _ in range(len(q)):
            curr_node = q.popleft()

            if curr_node.left: q.append(curr_node.left)
            if curr_node.right: q.append(curr_node.right)

    return result


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)
    result = tree_right_view(root)
    print("Tree right view: ")
    for node in result:
        print(str(node.val) + " ", end='')

