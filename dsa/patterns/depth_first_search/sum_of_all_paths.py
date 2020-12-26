"""
Given a binary tree where each node can only have a digit (0-9) value, 
each root-to-leaf path will represent a number. Find the total sum of 
all the numbers represented by all paths.
"""

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs(root, curr_sum, sum_of_paths):
    if not root:
        return sum_of_paths

    if not root.left and not root.right:
        curr_sum = curr_sum*10 + root.val
        sum_of_paths += curr_sum
        return sum_of_paths

    curr_sum = curr_sum*10 + root.val
    sum_of_paths = dfs(root.left, curr_sum, sum_of_paths)
    sum_of_paths = dfs(root.right, curr_sum, sum_of_paths)
    return sum_of_paths


def find_sum_of_path_numbers(root):
    sum_of_paths = 0
    return dfs(root, 0, sum_of_paths)

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    print("Total Sum: " + str(find_sum_of_path_numbers(root)))
