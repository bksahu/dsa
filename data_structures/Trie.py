"""
The following script implements a basic prefix tree structure.

Insert: O(n)
Search: O(n)

where, n = length of key
"""

class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def isTrieEmpty(self):
        return len(self.root.children) == 0

    def insert(self, word):
        curNode = self.root
        for ch in word:
            if ch not in curNode.children:
                curNode.children[ch] = TrieNode()
            curNode = curNode.children[ch]
        curNode.isEndOfWord = True

    def search(self, word):
        if self.isTrieEmpty():
            raise Exception("Trie is empty")
        curNode = self.root
        for ch in word:
            if ch not in curNode.children:
                return False
            curNode = curNode.children[ch]
        return curNode.isEndOfWord

    def delete(self, word):
        if not self.search(word):
            raise Exception("Word not found!")
        
        if self.isTrieEmpty():
            raise Exception("Trie is empty")

        curNode = self.root        
        for ch in word:
            if len(curNode.children[ch].children) == 1:
                curNode.children.pop(ch)
                break
            curNode = curNode.children[ch]
        curNode.isEndOfWord = False

            

if __name__ == "__main__":
    t = Trie()
    t.insert("Box")
    t.insert("Bottom")
    t.insert("Bat")
    print("Box Found: ", t.search("Box"))
    print("Batman Found: ", t.search("Batman"))
    t.delete("Box")
    print("Box Found: ", t.search("Box"))
    print("Bottom Found: ", t.search("Bottom"))
