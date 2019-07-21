class TrieNode:
    def __init__(self):
        self.children = {}
        self.index = -1

class Solution:
    """
    @param dict: List[str]
    @param sentence: a string
    @return: return a string
    """
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word, ind):
        head = self.root 
        for s in word:
            if s not in head.children:
                head.children[s] = TrieNode()
            # even if exits
            head = head.children[s]
        head.index = ind
        
    def buildTrie(self, dict):
        #   {   {   {   {
        # - c - a - t - #, ind
        # - b - a - t - #, ind
        #   }   }   }   }
        for ind, word in enumerate(dict):
            self.insert(word, ind)
        
    def search(self, word):
        head = self.root
        for s in word:
            if s not in head.children:
                return -1
            head = head.children[s]
            # head.index put after head.children[s]
            if head.index > -1:
                return head.index 
        return -1

    def replaceWords(self, dict, sentence):
        # O(nk)
        self.buildTrie(dict)
        sentence_list = sentence.split(' ')
        result = []
        for word in sentence_list:
            short_ind = self.search(word)
            if short_ind > -1:
                result.append(dict[short_ind])
            else:
                result.append(word)
                
        return ' '.join(result)
            
