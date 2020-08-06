"""
Given a sorted array, create a new array containing squares of all the number of the 
input array in the sorted order.

Example 1:
Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Example 2:
Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
"""
# def solution(arr):
#     return sorted([x*x for x in arr])

# Idea is to track the current highest number index
def solution(arr):
    left, right = 0, len(arr)-1
    res = [0 for _ in range(len(arr))]
    lastNumIdx = len(arr)-1

    while lastNumIdx >= 0:
        leftNum, rightNum = arr[left]**2, arr[right]**2
        if leftNum > rightNum:
            res[lastNumIdx] = leftNum
            left += 1
        else:
            res[lastNumIdx] = rightNum
            right -= 1
        lastNumIdx -= 1

    return res



if __name__ == "__main__":
    print(solution([-2, -1, 0, 2, 3]))
    print(solution([-3, -1, 0, 1, 2]))