class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # can no use memoization or DP 
        # coz DP[i][j] will change due to succeeding chars 
        # so use backtrack
        return self.helper(pattern, str, set(), {})
    
    # bijection, needs used to record words    
    def helper(self, pattern, str, used, mapping):
        if len(pattern) == 0:
            return len(str) == 0 
            
        char = pattern[0]
        if char in mapping:
            word = mapping[char]
            if not str.startswith(word):
                return False
            return self.helper(pattern[1:], str[len(word):], used, mapping)
            
        for i in range(1, len(str) + 1):
            word = str[:i]
            if word in used:
                continue 
            
            used.add(word)
            mapping[char] = word 
            matched = self.helper(pattern[1:], str[i:], used, mapping)
            if matched:
                return True 
                
            used.remove(word)
            del mapping[char]
            
        return False 
