"""
We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’. 
Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing 
number.

Example 1:
Input: [4, 0, 3, 1]
Output: 2

Example 2:
Input: [8, 3, 5, 2, 4, 6, 0, 1]
Output: 7
"""

# def find_missing_number(nums):
#     return list(set(range(len(nums))) - set(nums))[0]

def find_missing_number(nums):
    i = 0
    high = len(nums)
    while i < len(nums):
        if nums[i] == high:
            i += 1
        elif nums[i] != i:
            idx = nums[i] 
            nums[i], nums[idx] = nums[idx], nums[i]
        else:
            i += 1

    for i, num in enumerate(nums):
        if num == high:
            break

    return i


if __name__ == "__main__":
    print(find_missing_number([4, 0, 3, 1]))
    print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))