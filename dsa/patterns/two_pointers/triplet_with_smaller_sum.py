"""
Given an array arr of unsorted numbers and a target sum, count all triplets in it such
that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. 
Write a function to return the count of such triplets.

Example 1:

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
Example 2:

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]

"""
def search_pair(arr, firstIdx, target):
    first = arr[firstIdx]
    left, right = firstIdx+1, len(arr)-1
    curr_count = 0
    while left < right:
        if arr[left] + arr[right] + first < target:
            curr_count = right - left
            left += 1
        else:
            right -= 1

    return curr_count


def solution(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr)):
        count += search_pair(arr, i, target)
    return count


if __name__ == "__main__":
    print(solution([-1, 0, 2, 3], 3))
    print(solution([-1, 4, 2, 1, 3], 5))