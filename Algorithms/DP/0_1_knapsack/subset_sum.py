"""
Given a set of non-negative integers, and a value sum, determine if there is a
subset of the given set with sum equal to given sum.

Example:

Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
"""

def subset_sum_bool(arr, sum):
    # Return True if possible else False
    t = [[True if x == 0 else False for x in range(sum+1)] for x in range(len(arr) + 1)]
    
    for i in range(1, len(arr) + 1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                # check if such sum exist OR not
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
    
    return t[-1][-1]

if __name__ == "__main__":
    arr = [2,3,7,8,10]
    sum = 11
    print(subset_sum_bool(arr, sum))