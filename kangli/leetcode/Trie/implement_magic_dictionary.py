from collections import defaultdict


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.word_dict = defaultdict(list)

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            self.word_dict[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for potential_match in self.word_dict[len(word)]:
            mod_count = 0
            for i in range(len(word)):
                if word[i] != potential_match[i]:
                    mod_count += 1
            if mod_count == 1:
                return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)
'''
32 / 32 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 13.3 MB

Related Topics: Hash Table, Trie
Similar Questions: Implement Trie (Prefix Tree), Longest Word in Dictionary
'''
