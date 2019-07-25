class Solution:
    """
    @param strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        # O(kn)
        k = len(strs)
        if k == 0:
            return ''
        prev_str = strs[0]
        for i in range(1, k):
            prev_str = self.sliding_compare(prev_str, strs[i])
            if prev_str == '':
                return prev_str
            
        return prev_str
        
    def sliding_compare(self, str1, str2):
        start1, start2 = 0, 0 
        while start1 < len(str1) and start2 < len(str2):
            if str1[start1] == str2[start2]:
                start1 += 1 
                start2 += 1 
            else:
                break 
        
        return str1[:start1]
        
        
########## control end ########
class Solution:
    # @param strs: A list of strings
    # @return: The longest common prefix
    def longestCommonPrefix(self, strs):
        # write your code here
        if len(strs) <= 1:
            return strs[0] if len(strs) == 1 else ""
        end, minl = 0, min([len(s) for s in strs])
        while end < minl:
            for i in range(1, len(strs)):
                if strs[i][end] != strs[i-1][end]:
                    return strs[0][:end]
            end = end + 1
        return strs[0][:end]
        
        
