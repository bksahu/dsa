"""
Given a sequence originalSeq and an array of sequences, write a method to find if originalSeq can be uniquely 
reconstructed from the array of sequences.

Unique reconstruction means that we need to find if originalSeq is the only sequence such that all sequences in 
the array are subsequences of it.

Example 1:
Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [3, 4]]
Output: true
Explanation: The sequences [1, 2], [2, 3], and [3, 4] can uniquely reconstruct   
[1, 2, 3, 4], in other words, all the given sequences uniquely define the order of numbers 
in the 'originalSeq'. 

Example 2:
Input: originalSeq: [1, 2, 3, 4], seqs: [[1, 2], [2, 3], [2, 4]]
Output: false
Explanation: The sequences [1, 2], [2, 3], and [2, 4] cannot uniquely reconstruct 
[1, 2, 3, 4]. There are two possible sequences we can construct from the given sequences:
1) [1, 2, 3, 4]
2) [1, 2, 4, 3]

Example 3:
Input: originalSeq: [3, 1, 4, 2, 5], seqs: [[3, 1, 5], [1, 4, 2, 5]]
Output: true
Explanation: The sequences [3, 1, 5] and [1, 4, 2, 5] can uniquely reconstruct 
[3, 1, 4, 2, 5].
"""

from collections import deque

def can_construct(originalSeq, sequences):
    sortedOrder = []
    if len(originalSeq) <= 0:
        return sortedOrder
    inDegree = {i:0 for i in range(1, len(originalSeq)+1)}
    graph = {i:[] for i in range(1, len(originalSeq)+1)}

    for seq in sequences:
        for i in range(len(seq)-1):
            parent, child = seq[i], seq[i+1]
            if parent != child:
                graph[parent] += child,
                inDegree[child] += 1

    # if we don't have ordering rules for all numbers
    if len(originalSeq) != len(inDegree):
        return False

    sources = deque([v for v, d in inDegree.items() if d == 0])
    while sources:
        # if there are more than 1 source, it's not more unique
        if len(sources) > 1: return False
        # if next number is different from the original sequence
        if originalSeq[len(sortedOrder)] != sources[0]: return False
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)

    return len(sortedOrder) == len(originalSeq) # no unqiue way

if __name__ == "__main__":
    print("Can construct: " + str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " + str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " + str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))