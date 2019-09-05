class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        roots = set()
        for root in dict:
            roots.add(root)
        sentence = sentence.split(" ")
        res = []
        for i, word in enumerate(sentence):
            for j in range(len(word)):
                if word[0:j] in roots:
                    sentence[i] = word[0:j]
                    has_root = True
                    break
        return " ".join(sentence)


'''
Success
Details 
Runtime: 204 ms, faster than 43.08% of Python3 online submissions for Replace Words.
Memory Usage: 18.2 MB, less than 70.00% of Python3 online submissions for Replace Words.
Next challenges: Implement Trie (Prefix Tree)
'''
