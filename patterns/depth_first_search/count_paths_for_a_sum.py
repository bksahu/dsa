"""
Given a binary tree and a number ‘S’, find all paths in the tree such 
that the sum of all the node values of each path equals ‘S’. Please 
note that the paths can start or end at any node but all paths must 
follow direction from parent to child (top to bottom).
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def helper(root, S, currentPath):
    if not root:
        return 0

    currentPath.append(root.val)
    pathCount, pathSum = 0, 0

    for i in range(len(currentPath)-1, -1, -1):
        pathSum += currentPath[i]

        if pathSum == S:
            pathCount += 1

    pathCount += helper(root.left, S, currentPath)
    pathCount += helper(root.right, S, currentPath)
    
    currentPath.pop()
    return pathCount


def count_paths(root, S):
    return helper(root, S, [])

if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Tree has paths: " + str(count_paths(root, 11)))
