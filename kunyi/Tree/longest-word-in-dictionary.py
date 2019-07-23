########### queue ##########
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_final = False

class Solution:
    """
    @param words: a list of strings
    @return: the longest word in words that can be built one character at a time by other words in words
    """
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        head = self.root 
        for s in word:
            if s not in head.children:
                head.children[s] = TrieNode()
            head = head.children[s]
        head.is_final = True 
    
    def buildTrie(self, words):
        for word in words:
            self.insert(word)
        
    def longestWord(self, words):
        # Write your code here
        self.buildTrie(words)
        queue = []
        result = ''
        for prefix, node in self.root.children.items():
            if node.is_final:
                queue.append((prefix, node))
                
        while len(queue) > 0:
            tmp_result, head = queue.pop(0)
            if len(tmp_result) > len(result):
                result = tmp_result
            elif len(tmp_result) == len(result):
                result = min(tmp_result, result)
                
            for prefix, node in head.children.items():
                if node.is_final:
                    # ERROR
                    new_tmp_result = tmp_result + prefix 
                    queue.append((new_tmp_result, node))
                    
        return result

###### dict ###########
class Solution(object):
    # T(n) = O(2nlogn) + O(nk*k)
    def longestWord(self, words):
        words.sort()
        words.sort(key = len, reverse = True)
        res = []
        for word in words:
            temp = word
            for i in range(len(temp)):
                if temp[:len(temp) - i] in words:
                    if i == len(temp) - 1:
                        return temp
                else:
                    break       
        return ''
