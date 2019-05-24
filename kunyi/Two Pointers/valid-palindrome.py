###############      Method 1 continue  ###########################
class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        # Corner Case
        # we define empty string as valid palindrome?
        if s == '':
            return True 
            
        start, end = 0, len(s) - 1 
        while start < end:
            if not self.is_valid_scope(s[start]):
                start += 1 
                continue
            if not self.is_valid_scope(s[end]):
                end -= 1 
                continue
            if s[start].lower() != s[end].lower():
                return False 
            start += 1 
            end -= 1
            
        return True 
        
    def is_valid_scope(self, ch):
        # ord('a') - 97, ord('A') - 65
        if 0 <= ord(ch) - ord('a') < 26 or 0 <= ord(ch) - ord('A') < 26 or ch.isdigit():
            return True 
            
        return False
     
############### while in while #####################
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        start, end = 0, len(s) - 1
        while start < end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while start < end and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if start < end and s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
