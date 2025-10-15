# solution by @suyogk23 GITHUB
# a trie is a prefix tree that stores word efficiently(node of letters)
# create a node class with end bool flag and a next dict to store next nodes
# mark last letter nodes with end flag
class Node:
    def __init__(self, val=None, endFlag=False):
        self.endFlag = endFlag
        self.next={}

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.next:
                node.next[char] = Node()

            node = node.next[char]   

        node.endFlag = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.next:
                return False
            node = node.next[char]                
        return node.endFlag # true if end else false if not end letter

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for char in prefix:
            if char not in node.next:
                return False
            node = node.next[char]       
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
