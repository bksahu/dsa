"""
Given a set of numbers that might contain duplicates, find all of its distinct subsets.

Example 1:
Input: [1, 3, 3]
Output: [], [1], [3], [1,3], [3,3], [1,3,3]

Example 2:
Input: [1, 5, 3, 3]
Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 
"""

# def find_subsets(nums):
#     subsets = []

#     subsets.append([])
#     for currentNum in nums:
#         for i in range(len(subsets)):
#             currentSubset = list(subsets[i])
#             currentSubset.append(currentNum)
#             if currentSubset not in subsets:
#                 subsets.append(currentSubset)

#     return subsets


def find_subsets(nums):
    subsets = []

    nums.sort()
    subsets.append([])
    startIndex, endIndex = 0, 0
    for i in range(len(nums)):
        startIndex = 0
        if i > 0 and nums[i] == nums[i-1]:
            startIndex = endIndex + 1
        endIndex = len(subsets)-1
        for j in range(startIndex, endIndex+1):
            currentSubset = list(subsets[j])
            currentSubset.append(nums[i])
            subsets.append(currentSubset)

    return subsets

if __name__ == "__main__":
    print("Here is the list of subsets: " + str(find_subsets([1,3,3])))
    print("Here is the list of subsets: " + str(find_subsets([1,5,3,3])))