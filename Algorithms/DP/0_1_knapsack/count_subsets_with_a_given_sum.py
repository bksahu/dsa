"""
Count of subsets sum with a Given sum
Given an array arr[] of length N and an integer X, the task is to find the number of subsets with sum equal to X.
Example:

Input: arr[] = {1, 2, 3, 3}, X = 6
Output: 3
All the possible subsets are {1, 2, 3},
{1, 2, 3} and {3, 3}
"""
"""
Given a set of non-negative integers, and a value sum, determine if there is a
subset of the given set with sum equal to given sum.

Example:

Input:  set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output:  True  //There is a subset (4, 5) with sum 9.
"""

def count_subset_sum(arr, sum):
    # Return True if possible else False
    t = [[1 if x == 0 else 0 for x in range(sum+1)] for x in range(len(arr) + 1)]
    
    for i in range(1, len(arr) + 1):
        for j in range(1, sum+1):
            if arr[i-1] <= j:
                # check if such sum exist OR not
                t[i][j] = t[i-1][j] + t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]
    
    return t[-1][-1]

if __name__ == "__main__":
    arr = [1, 1, 1, 1]
    sum = 1
    print(count_subset_sum(arr, sum))
