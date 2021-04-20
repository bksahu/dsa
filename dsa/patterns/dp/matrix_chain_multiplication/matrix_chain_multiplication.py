"""
Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of 
dimension p[i-1] x p[i]. We need to write a function MatrixChainOrder() that should return 
the minimum number of multiplications needed to multiply the chain. 

Input: p[] = {40, 20, 30, 10, 30}   
Output: 26000  
There are 4 matrices of dimensions 40x20, 20x30, 30x10 and 10x30.
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
(A(BC))D --> 20*30*10 + 40*20*10 + 40*10*30

Input: p[] = {10, 20, 30, 40, 30} 
Output: 30000 
There are 4 matrices of dimensions 10x20, 20x30, 30x40 and 40x30. 
Let the input 4 matrices be A, B, C and D.  The minimum number of 
multiplications are obtained by putting parenthesis in following way
((AB)C)D --> 10*20*30 + 10*30*40 + 10*40*30

Input: p[] = {10, 20, 30}  
Output: 6000  
There are only two matrices of dimensions 10x20 and 20x30. So there 
is only one way to multiply the matrices, cost of which is 10*20*30
"""

def mcm(p):
    def findMinOp(i, j):
        if i == j:
            return 0

        minOp = float("inf")

        for k in range(i, j):
            minOp = min(
                minOp, 
                findMinOp(i, k) + p[i-1] * p[k] * p[j] + findMinOp(k+1, j)
            )
        return minOp

    cache = {}

    def findMinOpDP(i, j):
        if i == j:
            return 0

        if (i, j) in cache:
            return cache[(i, j)]

        cache[(i, j)] = float("inf")

        for k in range(i, j):
            cache[(i, j)] = min(
                cache[(i, j)], 
                findMinOpDP(i, k) + p[i-1] * p[k] * p[j] + findMinOpDP(k+1, j)
            )

        return cache[(i, j)]

    return findMinOpDP(1, len(p)-1)





if __name__ == "__main__":
    print(mcm([40, 20, 30, 10, 30]))
    print(mcm([10, 20, 30, 40, 30]))
    print(mcm([10, 20, 30]))
    print(mcm(list(range(2, 300, 3))))