"""
Given a binary tree and a number sequence, find if the 
sequence is present as a root-to-leaf path in the given tree.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root, currPos, sequence):
    if not root:
        return False

    if not root.left and not root.right and currPos == len(sequence)-1:
        if root.val == sequence[currPos]:
            return True
        return False

    if root.val != sequence[currPos]:
        return False

    return dfs(root.left, currPos+1, sequence) or dfs(root.right, currPos+1, sequence)

def find_path(root, sequence):
    return dfs(root, 0, sequence)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))