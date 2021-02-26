"""
The following script implements a basic union_find with Path Compression optimization & ranked.

find: O(1) to O(logn)
Union: O(1) to O(logn)
"""

if __name__ == "__main__":

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x]) # path compression
        return parent[x]

    def union(x, y):
        parentX, parentY = find(x), find(y)
        if rank[parentX] > rank[parentY]:
            parent[parentY] = parentX
            rank[parentX] += rank[parentY]
        else:
            parent[parentX] = parentY
            rank[parentY] += rank[parentX]

    nums = [1, 3, 2, 4, 0]
    n = len(nums)
    parent = list(range(n))
    rank = [1]*(n)
    
    for i in range(n-1):
        union(nums[i], nums[i+1])

    print(parent)
