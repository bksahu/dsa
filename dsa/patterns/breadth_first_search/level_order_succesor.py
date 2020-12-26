"""
Given a binary tree and a node, find the level order successor of the given node in the tree. The level order successor is the node that appears right after the given node in the level order traversal.
"""

import collections

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find_succesor(root, key):
    if not root: return
    found_key = False
    q = collections.deque([root])

    while q:
        level_size = len(q)
        for _ in range(level_size):
            curr_node = q.popleft()
            
            if found_key:
                return curr_node
            
            if curr_node.val == key:
                found_key = True

            if curr_node.left: q.append(curr_node.left)
            if curr_node.right: q.append(curr_node.right)
            
    return None


if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    result = find_succesor(root, 12)
    if result:
        print(result.val)
    
    result = find_succesor(root, 9)
    if result:
        print(result.val)
