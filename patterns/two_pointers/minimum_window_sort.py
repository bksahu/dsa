'''
Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

Example 1:
Input: [1, 2, 5, 3, 7, 10, 9, 12]
Output: 5
Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted

Example 2:
Input: [1, 3, 2, 0, -1, 7, 10]
Output: 5
Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted

Example 3:
Input: [1, 2, 3]
Output: 0
Explanation: The array is already sorted

Example 4:
Input: [3, 2, 1]
Output: 3
Explanation: The whole array needs to be sorted.
'''

# O(nlogn)
def solution1(arr):
    sorted_arr = sorted(arr)

    s, e = float("inf"), float("-inf")
    l, r = 0, len(arr)-1
    
    while l < len(arr):
        if arr[l] != sorted_arr[l]:
            s = l
            break
        l += 1

    if s == float("inf"):
        return 0
    
    while r >= 0:
        if arr[r] != sorted_arr[r]:
            e = r
            break
        r -= 1    

    return e - s + 1

# O(n)
def solution(arr):
    left, right = 0, len(arr)-1

    while left < len(arr)-1 and arr[left] <= arr[left+1]:
        left += 1

    if left == len(arr)-1: # it's sorted
        return 0

    while right > 0 and arr[right] >= arr[right-1]:
        right -= 1

    max_subarray_value, min_subarray_val = max(arr[left:right+1]), min(arr[left:right+1])

    while left > 0 and arr[left-1] > min_subarray_val:
        left -= 1
    
    while right < len(arr)-1 and arr[right+1] < max_subarray_value:
        right += 1

    return right - left + 1

if __name__ == "__main__":
    print(solution([1, 2, 5, 3, 7, 10, 9, 12]))
    print(solution([1, 3, 2, 0, -1, 7, 10]))
    print(solution([1,2,3]))
    print(solution([3,2,1]))
    print(solution([1,2,3,5,4]))