"""
Given a binary tree and a number ‘S’, find all paths from root-to-leaf such that the sum of all the node values of each path equals ‘S’.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def dfs(root, sum, currPath, allPaths):
    if not root:
        return

    if root.val == sum and not root.left and not root.right:
        currPath += root.val,
        allPaths += currPath,
    
    if root.left:
        dfs(root.left, sum-root.val, currPath+[root.val], allPaths)

    if root.right:
        dfs(root.right, sum-root.val, currPath+[root.val], allPaths)

def find_paths(root, sum):
    allPaths = []
    dfs(root, sum, [], allPaths)

    return allPaths

if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    sum = 23
    print("Tree paths with sum " + str(sum) + 
        ": " + str(find_paths(root, sum)))

