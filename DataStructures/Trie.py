"""
The following script implements a basic prefix tree structure.

Insert: O(n)
Search: O(n)

where, n = length of key
"""

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = self.getTrieNode()

    @staticmethod
    def getTrieNode(self):
        return TrieNode()

    @staticmethod
    def chDiff(self, ch):
        return ord(ch) - ord("A")

    def insert(self, word):
        pass