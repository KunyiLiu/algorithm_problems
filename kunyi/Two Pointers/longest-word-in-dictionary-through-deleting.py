class Solution(object):
    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        # T(n) = len(s) * len(d)
        # Space = max(len(s))
        result = ''
        for i in range(len(d)):
            if self.is_subsequence(s, d[i]):
                result = d[i] if len(d[i]) > len(result) or (len(d[i]) == len(result) and d[i] < result) else result
                
        return result 
    
    def is_subsequence(self, s, target):
        s_start, t_start = 0, 0 
        while s_start < len(s) and t_start < len(target):
            if s[s_start] == target[t_start]:
                s_start += 1 
                t_start += 1 
            else:
                s_start += 1 
                
        return t_start >= len(target)
