"""
Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists 
of numbers from both the arrays.

Example 1:
Input: L1=[9, 8, 2], L2=[6, 3, 1], K=3
Output: [9, 3], [9, 6], [8, 6] 
Explanation: These 3 pairs have the largest sum. No other pair has a sum larger than any of these.

Example 2:
Input: L1=[5, 2, 1], L2=[2, -1], K=3
Output: [5, 2], [5, -1], [2, 2] 
"""

from heapq import heappush, heappop

# # TC: O(M*NlogK) SP: O(K)
# def find_k_largest_pairs(num1, num2, k):
#     ret = []
#     minHeap = []
#     for i in range(len(num1)):
#         for j in range(len(num2)):
#             if len(minHeap) < k:
#                 heappush(minHeap, (num1[i] + num2[j], num1[i], num2[j]))
#             else:
#                 if num1[i] + num2[j] < minHeap[0][0]:
#                     break
#                 else:
#                     heappop(minHeap)
#                     heappush(minHeap, (num1[i] + num2[j], num1[i], num2[j]))

#     for _, i, j in minHeap:
#         ret.append([i, j])
    
#     return ret

def find_k_largest_pairs(num1, num2, k):
    """
    TC: O(K) 
    SP: O(K)
    Convert the arrays into a matrix and use BFS
    
    L1=[9, 8, 2], L2=[6, 3, 1], K=3

      |  6     3     1
    -------------------
    9 |  15    12    10
    8 |  14    11    9
    2 |  8     5     3
    """
    ret = []
    if len(num1) * len(num2) > 0:
        maxHeap = [(-num1[0] - num2[0], (0, 0))]
        visited = {}
        while len(ret) < k and maxHeap:
            _, (i, j) = heappop(maxHeap)
            ret.append([num1[i], num2[j]])
            if i+1 < len(num1) and (i+1, j) not in visited:
                heappush(maxHeap, (-num1[i+1] - num2[j], (i+1, j)))
                visited[(i+1, j)] = 1
            if j + 1 < len(num2) and (i, j + 1) not in visited:
                heappush(maxHeap, (-num1[i] - num2[j + 1], (i, j + 1)))
                visited[(i, j + 1)] = 1
    return ret


if __name__ == "__main__":
    print(find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3))
    print(find_k_largest_pairs([5, 2, 1], [2, -1], 3))