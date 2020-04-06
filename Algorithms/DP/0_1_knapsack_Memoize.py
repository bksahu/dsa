"""
Given weights and values of n items, put these items in
a knapsack of capacity W to get the maximum total value 
in the knapsack.

Constrains:
0 <= W <= 1000
0 <= n <= 100 
"""

def knapSack(W, wt, val, n):
    # If no more items is left
    # Or the knapsack is full
    if n == 0 or W == 0:
        cache[W][n] = 0
        return cache[W][n]

    # check if value alreay exists
    if cache[W][n] != -1:
        return cache[W][n]

    # If weight of the item is less
    # than the weight of the knapsack
    if wt[n-1] <= W:
        # return the max of two cases:
        # (1) nth item included
        # (2) item not included
        cache[W][n] = max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1)) 
        return cache[W][n]

    # If weight of the item is more than knapsack
    else:
        cache[W][n] = knapSack(W-wt[n-1], wt, val, n-1)
        return cache[W][n]

if __name__ == "__main__":
    # initialze a cache W*n for memoize
    global cache
    cache = [[-1 for x in range(102)] for x in range(1002)]

    # Dummy test case
    val = [60, 100, 120] 
    wt = [10, 20, 30] 
    W = 50
    n = len(val)
    print(knapSack(W , wt , val , n)) 