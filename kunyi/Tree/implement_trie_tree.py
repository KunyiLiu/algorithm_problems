class TrieNode:
    def __init__(self):
        self.childern = {}
        self.is_final = False

class Trie:
    
    def __init__(self):
        # do intialization if necessary
        self.root = TrieNode()

    """
    @param: word: a word
    @return: nothing
    """
    def insert(self, word):
        # write your code here
        head = self.root 
        for s in word:
            if s not in head.childern:
                head.childern[s] = TrieNode()  
            head = head.childern[s]
        head.is_final = True 

    """
    @param: word: A string
    @return: if the word is in the trie.
    """
    def search(self, word):
        # write your code here
        head = self.root 
        for s in word:
            if s not in head.childern:
                return False 
            head = head.childern[s]
            
        return head.is_final

    """
    @param: prefix: A string
    @return: if there is any word in the trie that starts with the given prefix.
    """
    def startsWith(self, prefix):
        # write your code here
        head = self.root 
        for s in prefix:
            if s not in head.childern:
                return False 
            head = head.childern[s]
            
        return True 
