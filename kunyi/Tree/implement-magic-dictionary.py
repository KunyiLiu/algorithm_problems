class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_final = False

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            head = self.root
            for s in word:
                if s not in head.children:
                    head.children[s] = TrieNode()
                head = head.children[s]
            head.is_final = True
            
    def contains(self, word: str) -> bool:
        head = self.root
        for s in word:
            if s not in head.children:
                return False
            head = head.children[s]
        return head.is_final      

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        # first layer TrieNode list
        head_list = [self.root]
        for i, s in enumerate(word):
            tmp_list = []
            for head in head_list:
                for char, node in head.children.items():
                    if char != s:
                        if self.contains(word[:i] + char + word[(i+1):]):
                            return True 
                    tmp_list.append(node)
            # next layer TrieNode list
            head_list = tmp_list
        return False     

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
