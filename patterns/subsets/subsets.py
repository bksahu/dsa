"""
Given a set with distinct elements, find all of its distinct subsets.

Example 1:
Input: [1, 3]
Output: [], [1], [3], [1,3]

Example 2:
Input: [1, 5, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]
"""

# def find_subsets(nums):
#     subsets = []
#     dfs(nums, 0, [], subsets)
#     return subsets

# def dfs(nums, idx, path, subsets):
#     subsets.append(path)
#     for i in range(idx, len(nums)):
#         dfs(nums, i+1, path+[nums[i]], subsets)

def find_subsets(nums):
    subsets = []

    subsets.append([])
    for currentNumber in nums:
        for i in range(len(subsets)):
            currentSet = list(subsets[i])
            currentSet.append(currentNumber)
            subsets.append(currentSet)

    return subsets

if __name__ == "__main__":
    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1,5,3])))