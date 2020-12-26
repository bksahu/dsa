"""
Find the minimum depth of a binary tree. The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.
"""

import collections

class Solution:
    def minDepth(self, root) -> int:
        if not root: return 0
        minDepth = float("inf")
        q = collections.deque([(root, 1)])
        
        while q:
            levelSize = len(q)
            for _ in range(levelSize):
                currNode, depth = q.popleft()
                
                if not currNode.left and not currNode.right:
                    minDepth = min(minDepth, depth)
                    
                if currNode.left: 
                    q.append((currNode.left, depth+1))                                        
                    
                if currNode.right:
                    q.append((currNode.right, depth+1))
        return minDepth