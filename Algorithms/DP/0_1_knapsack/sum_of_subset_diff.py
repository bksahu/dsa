"""
Sum of subset differences
Given a set of integers, the task is to divide it into two sets S1 and S2 such that the absolute difference between their sums is minimum.
If there is a set S with n elements, then if we assume Subset1 has m elements, Subset2 must have n-m elements and the value of abs(sum(Subset1) – sum(Subset2)) should be minimum.

Example:
Input:  arr[] = {1, 6, 11, 5} 
Output: 1
Explanation:
Subset1 = {1, 5, 6}, sum of Subset1 = 12 
Subset2 = {11}, sum of Subset2 = 11 
"""

def min_subset_diff(arr):
    target, n = sum(arr), len(arr)
    dp = [[True if x == 0 else False for x in range(target + 1)] for x in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, target + 1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j] or dp[i-1][j-arr[i-1]]
            else:
                dp[i][j] = dp[i-1][j]
    
    mid = (target+1) >> 1
    dp = dp[-1]
    while dp[mid] != True:
        mid -= 1

    return abs(target-2*mid)



if __name__ == "__main__":
    arr = [1,2,7]
    print(min_subset_diff(arr))