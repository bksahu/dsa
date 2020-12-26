"""
Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and 
then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

Example 1:
Input: [1, 3, 8, 12, 4, 2]
Output: 12
Explanation: The maximum number in the input bitonic array is '12'.

Example 2:
Input: [3, 8, 3, 1]
Output: 8

Example 3:
Input: [1, 3, 8, 12]
Output: 12

Example 4:
Input: [10, 9, 8]
Output: 10
"""

def find_max_in_bitonic_array(arr):
    """
      
    """
    left, right = 0, len(arr)-1
    while left < right:
        mid = left + (right - left)//2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            right = mid 

    return arr[left]

if __name__ == "__main__":
    print(find_max_in_bitonic_array([1, 3, 8, 12, 4, 2]))
    print(find_max_in_bitonic_array([3, 8, 3, 1]))
    print(find_max_in_bitonic_array([1, 3, 8, 12]))
    print(find_max_in_bitonic_array([10, 9, 8]))
    print(find_max_in_bitonic_array([1, 2, 8, 8, 3, 1]))