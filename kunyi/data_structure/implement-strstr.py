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

    
    
    # KMP
    class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        # KMP O(n)
        # lps[i] = the longest proper prefix of pat[0..i] 
        # which is also a suffix of pat[0..i]
        len_s, len_t = len(source), len(target)
        lps = [0] * len_t
        j = 0  # for target 
        i = 0
        
        if len_t == 0:
            return 0
        
        self.compute_lps(target, len_t, lps)
        while i < len_s:
            if target[j] == source[i]:
                i += 1 
                j += 1 
            if j == len_t:
                return i - len_t
            # mismatch after j matches
            elif i < len_s and target[j] != source[i]:
                # target[0, ...lps[j-1] match 
                # target prfix, AAAD
                # source suffix ...AAACAAAADA
                
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1 
        return -1 
        
    def compute_lps(self, target, len_t, lps):
        longest = 0
        # lps[0] = 0 
        i = 1
        while i < len_t:
            if target[i] == target[longest]:
                longest += 1 
                lps[i] = longest
                i += 1 
            else:
                # AAACAAAA heads to i= 3, longest = 2, lps[0,1,2]
                if longest != 0:
                    longest = lps[longest - 1]
                else:
                    lps[i] = 0
                    i += 1 
        
        
        
