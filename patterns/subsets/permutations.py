"""
Given a set of distinct numbers, find all of its permutations.

Permutation is defined as the re-arranging of the elements of the set. For example, 
{1, 2, 3} has the following six permutations:

{1, 2, 3}
{1, 3, 2}
{2, 1, 3}
{2, 3, 1}
{3, 1, 2}
{3, 2, 1}
If a set has ‘n’ distinct elements it will have n!n! permutations.

Example 1:

Input: [1,3,5]
Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]
"""

def find_permutations_recursively(nums):
    results = []
    backtrack(nums, [], results)
    return results

def backtrack(nums, tempList, results):
    if len(tempList) == len(nums):
        copyList = tempList.copy()
        results += copyList,
    else:
        for num in nums:
            if num not in tempList:
                tempList += num,
                backtrack(nums, tempList, results)
                tempList.pop()

from collections import deque

def find_permutations(nums):
    results = []
    permutations = deque()
    permutations.append([])
    import ipdb; ipdb.set_trace()
    for currentNum in nums:
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            for j in range(len(oldPermutation)+1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, currentNum)
                if len(newPermutation) == len(nums):
                    results.append(newPermutation)
                else:
                    permutations.append(newPermutation)
    return results


if __name__ == "__main__":
    print("Here are all the permutations: " + str(find_permutations([1,3,5])))