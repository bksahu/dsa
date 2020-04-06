"""
Given weights and values of n items, put these items in
a knapsack of capacity W to get the maximum total value 
in the knapsack.

Constrains:
0 <= W <= 1000
0 <= n <= 100 
"""

def knapSack(W, wt, val, n):
    # Table where we will store values
    dp = [[0 for x in range(W+1)] for x in range(n+1)] 


    for i in range(n+1):
        for j in range(W+1):
            # Initialize the base case
            if i == 0 or j == 0:
                dp[i][j] = 0
            # if weight is less than the knapsack
            # weight in the current state
            elif wt[i-1] <= j:
                dp[i][j] = max(
                    val[i-1] + dp[i-1][j-wt[i-1]],
                    dp[i-1][j]
                )
            else:
                dp[i][j] = dp[i-1][j]

    return dp




if __name__ == "__main__":

    # Dummy test case
    val = [60, 100, 120] 
    wt = [10, 20, 30] 
    W = 50
    n = len(val)
    print(knapSack(W , wt , val , n)) 