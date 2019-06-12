class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # Write your code here
        len_s, len_t = len(source), len(target)
        if len_t > len_s:
            return -1 
        if len_s == 0 or len_t == 0:
            return 0
        for i in range(len_s - len_t + 1):
            if source[i] != target[0]:
                continue
            if self.is_target(source[i:(i+len_t)], target):
                return i 
                
        return -1 
        
    def is_target(self, substring, target):
        for i in range(1, len(target)):
            if substring[i] != target[i]:
                return False 
                
        return True
