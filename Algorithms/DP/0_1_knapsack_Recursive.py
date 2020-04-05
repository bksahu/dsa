"""
Given weights and values of n items, put these items in
a knapsack of capacity W to get the maximum total value 
in the knapsack.
"""

def knapSack(W, wt, val, n):
    # If no more items is left
    # Or the knapsack is full
    if n == 0 or W == 0:
        return 0

    # If weight of the item is less
    # than the weight of the knapsack
    if wt[n-1] <= W:
        # return the max of two cases:
        # (1) nth item included
        # (2) item not included
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1)) 
    # If weight of the item is more than knapsack
    else:
        return knapSack(W-wt[n-1], wt, val, n-1)


if __name__ == "__main__":
    val = [60, 100, 120] 
    wt = [10, 20, 30] 
    W = 50
    n = len(val)
    print(knapSack(W , wt , val , n)) 