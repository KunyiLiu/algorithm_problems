class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = Trie()
        res = []
        sentence = sentence.split(" ")
        for i, word in enumerate(dict):
            trie.insert(word, i)
        for word in sentence:
            index = trie.prefix_search(word)
            if index is not None:
                res.append(dict[index])
            else:
                res.append(word)
        return " ".join(res)
                                
class Trie:
    def __init__(self):
        self.children = {}
    
    def insert(self, word, index):
        root = self.children
        for c in word:
            if c not in root:
                root[c] = {}
            root = root[c]
        root['index'] = index
    
    def prefix_search(self, word):
        root = self.children
        for c in word:
            if c not in root:
                if 'index' in root:
                    return root['index']
                else:
                    return None
            else:
                if 'index' in root:
                    return root['index']
                root=root[c]
            
'''
Success
Details 
Runtime: 80 ms, faster than 82.07% of Python3 online submissions for Replace Words.
Memory Usage: 27.3 MB, less than 37.96% of Python3 online submissions for Replace Words.
Next challenges:
Sudoku Solver
Happy Number
Subarray Sums Divisible by K
'''
