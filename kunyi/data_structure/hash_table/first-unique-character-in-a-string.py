class Solution:
    """
    @param str: str: the given string
    @return: char: the first unique character in a given string
    """
    def firstUniqChar(self, str):
        # Write your code here
        from collections import Counter 
        char_counter = Counter(str)
        
        for charac in str:
            if char_counter[charac] == 1:
                return charac
                
        return
