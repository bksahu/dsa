'''
Given a string of size ‘n’. The task is to remove or delete minimum number of characters 
from the string so that the resultant string is palindrome.

Examples :
Input : aebcbda
Output : 2

Remove characters 'e' and 'd'
Resultant string will be 'abcba'
which is a palindromic string
'''

def min_delete(s):
    n = len(s)
    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    rev_s = s[::-1]
    for i in range(1, n+1):
        for j in range(1, n+1):
            if s[i-1] == rev_s[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return len(s) - dp[-1][-1]

print(min_delete("aebcbda"))