"""
Given an array of unsorted numbers and a target number, find all unique 
quadruplets in it, whose sum is equal to the target number.

Example 1:
Input: [4, 1, 2, -1, 1, -3], target=1
Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
Explanation: Both the quadruplets add up to the target.

Example 2:
Input: [2, 0, -1, 1, -2, 2], target=2
Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
Explanation: Both the quadruplets add up to the target.
"""

def solution(arr, target):
    arr.sort()
    res = []
    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr)-2):
            if j > 0 and arr[j] == arr[j-1]:
                continue
            search_pair(arr, res, i, j, target)

    return res

def search_pair(arr, res, firstIdx, secondIdx, target):
    left = secondIdx+1
    right = len(arr)-1
    while left < right:
        curr_arr = [arr[firstIdx], arr[secondIdx], arr[left], arr[right]]
        if sum(curr_arr) == target:
            res.append(curr_arr)
            left += 1
            right -= 1
            while left < right and arr[left] == arr[left-1]: left+=1
            while left < right and arr[right] == arr[right+1]: right-=1
        elif sum(curr_arr) < target:
            left += 1
        else:
            right -= 1

if __name__ == "__main__":
    print(solution([4, 1, 2, -1, 1, -3], 1))
    print(solution([2, 0, -1, 1, -2, 2], 2))