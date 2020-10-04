"""

You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
    int val;
    Node *left;
    Node *right;
    Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

import collections

class Solution:
    def connect(self, root):
        if not root: return root
        q = collections.deque([root])
        
        while q:
            currSize = len(q)
            prevNode = None
            for _ in range(currSize):
                currNode = q.popleft()
                
                if prevNode:
                    prevNode.next = currNode
                prevNode = currNode
                
                if currNode.left: q.append(currNode.left)
                if currNode.right: q.append(currNode.right)
            
            
        return root