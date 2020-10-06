"""
Given a binary tree and a number ‘S’, find if the tree has a path from root-to-leaf 
such that the sum of all the node values of that path equals ‘S’.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path(root, sum):
    if not root:
        return False

    if not root.left and not root.right and sum == root.val:
        return True
    
    return has_path(root.right, sum-root.val) or has_path(root.left, sum-root.val)

def has_path_stack(root, sum):
    

if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has path: " + str(has_path(root, 23)))
    print("Tree has path: " + str(has_path(root, 16)))