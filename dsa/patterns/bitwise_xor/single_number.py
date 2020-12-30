"""
In a non-empty array of integers, every number appears twice except for one, find that single number.

Example 1:
Input: 1, 4, 2, 1, 3, 2, 3
Output: 4

Example 2:
Input: 7, 9, 7
Output: 9
"""

def find_single_number(nums):
    single_num = nums[0]
    for i in range(1, len(nums)):
        single_num ^= nums[i]
    return single_num

if __name__ == "__main__":
    print(find_single_number([1, 4, 2, 1, 3, 2, 3]))
    print(find_single_number([7, 9, 7]))