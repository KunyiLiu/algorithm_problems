############### set up a count to keep track of the time of deleting ############
class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        #  lowercase characters
        start, end = 0, len(s) - 1 
        count = 0
        while start < end:
            if s[start].lower() == s[end].lower():
                start += 1 
                end -= 1 
            else:
                if s[end-1] == s[start]:
                    # remove end 
                    end -= 1 
                    count += 1 
                elif s[start+1] == s[end]:
                    # remove start 
                    start += 1 
                    count += 1 
                else:
                    # not match right away
                    return False 
                    
        return count <= 1 
        
 ############ manually try second match after the first remove ##############
 class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """
    def validPalindrome(self, s):
        # Write your code here
        start, end = 0, len(s) - 1 
        while start < end:
            if s[start] != s[end]:
                break 
            start += 1 
            end -= 1 
            
        if start >= end:
            return True 
            
        # hit first unmatch 
        # delete left or right 
        return self.is_palindrome(s, start + 1, end) or self.is_palindrome(s, start, end - 1)
        
    def is_palindrome(self, s, start, end):
        while start < end:
            if s[start] != s[end]:
                return False 
                
            start += 1 
            end -= 1 
            
        return True 
