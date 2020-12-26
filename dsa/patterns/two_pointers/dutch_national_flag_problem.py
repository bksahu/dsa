"""
Given an array containing 0s, 1s and 2s, sort the array in-place. You should 
treat numbers of the array as objects, hence, we can’t count 0s, 1s, and 2s 
to recreate the array.

The flag of the Netherlands consists of three colors: red, white and blue; and 
since our input array also consists of three different numbers that is why it 
is called Dutch National Flag problem.

Example 1:
Input: [1, 0, 2, 1, 0]
Output: [0 0 1 1 2]

Example 2:
Input: [2, 2, 0, 1, 2, 0]
Output: [0 0 1 2 2 2 ]
"""

def solution(arr):
    zero_pointer, two_pointer = 0, len(arr)-1

    i = 0
    while i <= two_pointer:
        if arr[i] == 0:
            arr[i], arr[zero_pointer] = arr[zero_pointer], arr[i]
            i += 1
            zero_pointer += 1
        elif arr[i] == 1:
            i += 1
        else:
            arr[i], arr[two_pointer] = arr[two_pointer], arr[i]
            two_pointer -= 1
    return arr

if __name__ == "__main__":
    print(solution([1, 0, 2, 1, 0]))
    print(solution([2, 2, 0, 1, 2, 0]))