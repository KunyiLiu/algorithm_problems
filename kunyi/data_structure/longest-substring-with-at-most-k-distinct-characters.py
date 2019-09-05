class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        # use char_count_dict to record unique chars 
        # {e: 1}, {e: 1, c: 1} , {e: 2, c: 1, b: 1} 
        # if len(keys) <= k, end += 1, update result and dict 
        #              > k, start += 1, update dict, if dict[start] == 0 remove 
        #                    if start == end: 
        # ece, k = 1 
        start, end = 0, 0 
        char_count_dict = {}
        result = 0 
        while start < len(s) and end < len(s):
            if len(char_count_dict) < k or (len(char_count_dict) == k and s[end] in char_count_dict):
                char_count_dict[s[end]] = char_count_dict.get(s[end], 0) + 1 
                end += 1
                result = max(result, end - start)
            else:
                if start == end:
                    start += 1 
                    end += 1 
                else:
                    char_count_dict[s[start]] -= 1 
                    if char_count_dict[s[start]] == 0:
                        del char_count_dict[s[start]]
                    start += 1 
                    
        return result
        
        
 ##  modify left bound ######
 class Solution:
    """
    @param s: A string
    @param k: An integer
    @return: An integer
    """
    def lengthOfLongestSubstringKDistinct(self, s, k):
        if not s:
            return 0
            
        counter = {}
        left = 0
        longest = 0
        for right in range(len(s)):
            counter[s[right]] = counter.get(s[right], 0) + 1
            while left <= right and len(counter) > k:
                counter[s[left]] -= 1
                if counter[s[left]] == 0:
                    del counter[s[left]]
                left += 1
            
            longest = max(longest, right - left + 1)
        return longest
