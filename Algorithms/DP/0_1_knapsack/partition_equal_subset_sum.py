"""
Partition problem is to determine whether a given set can be partitioned into two subsets such that the sum of elements in both subsets is same.
Examples:

arr[] = {1, 5, 11, 5}
Output: true 
The array can be partitioned as {1, 5, 5} and {11}
"""

def partition_equal_subset_sum(arr):
    target, n = sum(arr), len(arr)
    if target & 1: return False
    target >>= 1
    
    t = [[True if x == 0 else False for x in range(target+1)] for x in range(n + 1)]

    for i in range(1, n+1):
        for j in range(1, target+1):
            if arr[i-1] <= j:
                t[i][j] = t[i-1][j] or t[i-1][j-arr[i-1]]
            else:
                t[i][j] = t[i-1][j]

    return t[-1][-1]



if __name__ == "__main__":
    arr = [1,5,11,5]
    print(partition_equal_subset_sum(arr))