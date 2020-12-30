"""
In a non-empty array of numbers, every number appears exactly twice except two numbers that 
appear only once. Find the two numbers that appear only once.

Example 1:
Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
Output: [4, 6]

Example 2:
Input: [2, 1, 3, 2]
Output: [1, 3]
"""
import collections

# def find_single_numbers(nums):
#     c = collections.Counter(nums)
#     res = []
#     for k, v in c.items():
#         if v == 1:
#             res += k,

#     return res

def find_single_numbers(nums):
    n1xn2 = 0
    for num in nums:
        n1xn2 ^= num

    rightSetBit = 1
    while (rightSetBit & n1xn2) == 0:
        rightSetBit <<= 1
    num1, num2 = 0, 0

    for num in nums:
        if num & rightSetBit == 0:
            num1 ^= num
        else:
            num2 ^= num

    return [num1, num2]

if __name__ == "__main__":
    print(find_single_numbers([1, 4, 2, 1, 3, 5, 6, 2, 3, 5]))
    print(find_single_numbers([2, 1, 3, 2]))