"""
Given a string, a partitioning of the string is a palindrome partitioning if every substring of the partition is a palindrome. 
For example, “aba|b|bbabb|a|b|aba” is a palindrome partitioning of “ababbbabbababa”. Determine the fewest cuts needed for a 
palindrome partitioning of a given string. For example, minimum of 3 cuts are needed for “ababbbabbababa”. The three cuts are 
“a|babbbab|b|ababa”. If a string is a palindrome, then minimum 0 cuts are needed. If a string of length n containing all different 
characters, then minimum n-1 cuts are needed. 
"""

def palindromePartition(s):
    def isPalindrome(x):
        return x[::-1] == x

    def backtrack(i, j):
        if i >= j or isPalindrome(s[i:j+1]):
            return 0

        minCuts = float("inf")

        for k in range(i, j):
            minCuts = min(
                    minCuts,
                    1 + backtrack(i,k) + backtrack(k+1, j)
                )

        return minCuts

    return backtrack(0, len(s)-1)


if __name__ == "__main__":
    print(palindromePartition("geek"))
    print(palindromePartition("aaaa"))
    print(palindromePartition("abcde"))
    print(palindromePartition("abbac"))