class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_final = False 

class WordDictionary:
    """
    @param: word: Adds a word into the data structure.
    @return: nothing
    """
    head = TrieNode()
    
    def addWord(self, word):
        # write your code here
        node = self.head 
        for w in word:
            if w not in node.children:
                node.children[w] = TrieNode()
                
            node = node.children[w]
        node.is_final = True 

    """
    @param: word: A word could contain the dot character '.' to represent any one letter.
    @return: if the word is in the data structure.
    """
    def search(self, word):
        # Time: O(kn)
        # search using iteration, more straightword, but needs more space 
        node_list = [self.head] 
        for w in word:
            if w == '.':
                node_list = [child for node in node_list for child in node.children.values()]
            else:
                tmp = []
                for node in node_list:
                    if w in node.children:
                        tmp.append(node.children[w])
                
                node_list = tmp 
    
            if len(node_list) == 0:
                return False 
                
        for node in node_list:
            if node.is_final:
                return True 
                
        return False 
        
#  using recursion, less space (stack space can be ignored, or use tail recursion to improve process). 
#  cons: may cause stackoverflow 
# In python, even with tail recursion(call function itself), will not have any effect
# where the function calls itself at the end ("tail") of the function in which no computation is done
# after the return of recursive call.

   def search(self, word):
        if word is None:
            return False
        return self.search_helper(self.root, word, 0)
        
    def search_helper(self, node, word, index):
        if node is None:
            return False
            
        if index >= len(word):
            return node.is_word
        
        char = word[index]
        if char != '.':
            return self.search_helper(node.children.get(char), word, index + 1)
            
        for child in node.children:
            if self.search_helper(node.children[child], word, index + 1):
                return True
                
        return False
        
   
