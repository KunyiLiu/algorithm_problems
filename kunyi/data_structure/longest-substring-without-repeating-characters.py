##### Method 1 O(len(s) #####
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # write your code here
        if len(s) == 0:
            return 0
        unique_char_set = set()
        start, end = 0, 0 
        result = 0
        while start < len(s) and end < len(s):
            if s[end] not in unique_char_set:
                unique_char_set.add(s[end])
                end += 1 
                
            else:
                # now unique_char_set is empty
                if start == end:
                    start += 1 
                    end += 1 
                else:
                    unique_char_set.remove(s[start])
                    start += 1 
                    
                
            result = max(result, end - start)
            
        return result
        
####### hash table ######
class Solution:
    """
    @param s: a string
    @return: an integer
    """
    def lengthOfLongestSubstring(self, s):
        # doouble pointer, traverse once respectively
        # O(n)
        # using [0]*26 to record the number of character appearance similar to sliding window not all uppercase
        char_hash = {}
        if len(s) == 0:
            return 0
        l, r = 0, 0
        char_hash[s[l]] = 1 
        result = 1
        while l <= r and r < len(s) - 1 :
            result = result if (r - l + 1) < result else (r - l + 1)
            if s[r+1] in char_hash and l < r:
                del char_hash[s[l]]
                l += 1
            elif s[r+1] in char_hash and l == r:
                del char_hash[s[l]]
                l += 1
                r += 1 
                char_hash[s[r]] = 1 
            else:
                r += 1 
                char_hash[s[r]] = 1 
        result = result if (r - l + 1) < result else (r - l + 1)
        return result
