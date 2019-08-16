class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        string_hash, pattern_hash = {}, {}
        string = string.split(" ")
        if len(string) != len(pattern):
            return False
        for i, c in enumerate(pattern):
            if c not in pattern_hash:
                pattern_hash[c] = [i]
            else:
                pattern_hash[c].append(i)

        for i, word in enumerate(string):
            if word not in string_hash:
                string_hash[word] = [i] 
            else:
                string_hash[word].append(i)
        
        for c, word in zip(pattern, string):
            print(c)
            if pattern_hash[c] != string_hash[word]:
                return False
        return True
        
        
'''
Success
Details 
Runtime: 36 ms, faster than 65.73% of Python3 online submissions for Word Pattern.
Memory Usage: 13.9 MB, less than 5.55% of Python3 online submissions for Word Pattern.
Next challenges:
Isomorphic Strings
Word Pattern II
'''
