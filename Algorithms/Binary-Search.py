"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and 
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value, start=0, end=None):
    """return sorted array"""
    if end is None:
        end = len(input_array) - 1
    if start > end:
        return False
    
    mid = (start + end) // 2
    if value == input_array[mid]:
        return mid
    if input_array[mid] > value:
        return binary_search(input_array, value, start, mid-1)
    
    return binary_search(input_array, value, mid+1, end)

test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)