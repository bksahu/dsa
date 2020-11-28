"""
Given weights and values of n items, put these items in
a knapsack of capacity W to get the maximum total value 
in the knapsack.

NOTE: We can have multiple occurance of the same item.

Constrains:
0 <= W <= 1000
0 <= n <= 100 
"""
def unboundedKnapsack(W, wt, val, n):
    dp = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if wt[i-1] <= j:
                dp[i][j] = max(dp[i-1][j], val[i-1] + dp[i][j - wt[i-1]]) # as we can have multiple occurances of items
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]


if __name__ == "__main__":
    # Dummy test case
    val = [1, 30] 
    wt = [1, 50] 
    W = 100
    n = len(val)
    print(unboundedKnapsack(W , wt , val , n)) 