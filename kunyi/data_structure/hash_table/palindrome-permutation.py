class Solution:
    """
    @param s: the given string
    @return: if a permutation of the string could form a palindrome
    """
    def canPermutePalindrome(self, s):
        # counter {a: 2, b: 1 } 
        # only one or none odd count 
        from collections import Counter 
        counter = Counter(s)
        odd_count = 0 
        for key, count in counter.items():
            if count % 2 == 1:
                odd_count += 1 
                
            if odd_count > 1:
                return False 
                
        return True
