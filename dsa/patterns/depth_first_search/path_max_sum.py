"""
Find the path with the maximum sum in a given binary tree. Write a function that returns the maximum sum. 
A path can be defined as a sequence of nodes between any two nodes and doesn’t necessarily pass through the root.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class MaximumPathSum:
    def __init__(self):
        self.maxPathSum = float("-inf")

    def find_maximum_path_sum(self, root):
        self.find_sums(root)
        return self.maxPathSum

    def find_sums(self, root):
        if not root:
            return 0

        leftMax = max(self.find_sums(root.left), 0)
        rightMax = max(self.find_sums(root.right), 0)

        self.maxPathSum = max(self.maxPathSum, root.val + leftMax + rightMax)

        return max(leftMax, rightMax) + root.val


if __name__ == "__main__":
    maximum_path_sum = MaximumPathSum()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    print("Maximum Path Sum: " + str(maximum_path_sum.find_maximum_path_sum(root)))
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.left.left = TreeNode(7)
    root.right.left.right = TreeNode(8)
    root.right.right.left = TreeNode(9)
    print("Maximum Path Sum: " + str(maximum_path_sum.find_maximum_path_sum(root)))

    root = TreeNode(-1)
    root.left = TreeNode(-3)
    print("Maximum Path Sum: " + str(maximum_path_sum.find_maximum_path_sum(root)))