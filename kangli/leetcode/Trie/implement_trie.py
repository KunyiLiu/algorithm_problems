class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.children
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = '#'

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.children
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return True if '#' in cur else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.children
        for c in prefix:
            if c not in cur:
                return False
            cur = cur[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

'''

15 / 15 test cases passed.
Status: Accepted
Runtime: 96 ms
Memory Usage: 24.8 MB

Related Topics: Design, Trie
Similar Questions: 
Add and Search Word - Data structure design, Design Search Autocomplete System, 
Replace Words, Implement Magic Dictionary
'''
