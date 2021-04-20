"""
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller than n. 
Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example, if length of the 
rod is 8 and the values of different pieces are given as following, then the maximum obtainable value is 22 (by 
cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 1   5   8   9  10  17  17  20
And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces of length 1)

length   | 1   2   3   4   5   6   7   8  
--------------------------------------------
price    | 3   5   8   9  10  17  17  20
"""

def cutRod(arr, size):
    # rows are the rod size. cols are prices
    dp = [[0 for x in range(size+1)] for x in range(size+1)]

    for i in range(1, size+1):
        for j in range(1, size+1):
            if i <= j:
                # maximum between cutting the rod at i and not cutting
                # the rod. dp[i][j-i] represents the profit of remaining
                # part
                dp[i][j] = max(dp[i-1][j], arr[i-1] + dp[i][j - i])
            else:
                dp[i][j] = dp[i-1][j]

    return dp[-1][-1]

# def cutRod(arr, size):
#     dp = [0 for x in range(size+1)]

#     for i in range(1, size+1):
#         _max = -float("inf")
#         for j in range(i):
#             _max = max(_max, arr[j] + dp[i - 1 - j])
#         dp[i] = _max
#         print(dp)

#     return dp[size]

if __name__ == "__main__":
    arr = [1, 5, 8, 9, 10, 17, 17, 20] 
    size = len(arr) 
    print("Maximum Obtainable Value is", cutRod(arr, size))