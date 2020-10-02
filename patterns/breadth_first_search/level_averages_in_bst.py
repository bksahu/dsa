"""
Given a binary tree, populate an array to represent the averages of all of its levels.
"""

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def find_level_average(root):
    result = []
    q = deque([root])

    while q:
        currLevelSize = len(q)
        currLevelSum = 0.0
        for _ in range(currLevelSize):
            currNode = q.popleft()
            currLevelSum += currNode.val
            if currNode.left: q.append(currNode.left)
            if currNode.right: q.append(currNode.right)
        result.append(currLevelSum / currLevelSize)

    return result

if __name__ == "__main__":
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    print("Level averages are: " + str(find_level_average(root)))