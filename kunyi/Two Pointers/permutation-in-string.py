############# TLE #####################
######  O(n2) ###################
class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # hashtable for s1 {char: count}
        count = dict()
        for char in s1:
            if char not in count:
                count[char] = 0
            count[char] += 1 
        
        start, end = 0, 0   
        while start < len(s2) and end < len(s2):
            if count.get(s2[start], 0) == 0:
                start += 1 
                end += 1 
            else:
                tmp = count.copy()
                tmp[s2[start]] -= 1
                end += 1
                while end < len(s2) and tmp.get(s2[end], 0):
                    tmp[s2[end]] -= 1
                    if end - start + 1 == len(s1):
                        return True
                    end += 1 
                start += 1 
                end = start 
        return False
        
 ################## sliding window ##########################
 ################ Rabin Karp ##########################
 class Solution:
    """
    @param s1: a string
    @param s2: a string
    @return: if s2 contains the permutation of s1
    """
    def checkInclusion(self, s1, s2):
        # reference to find-all-anagrams-in-a-string
        # set up a sliding window with size of len(s1) in s2
        # compare the sorted version with s1
        if len(s1) > len(s2):
            return False 
        sorted_s1 = [0] * 26  # 26 characters 
        sorted_s2 = [0] * 26 
        n, m = len(s1), len(s2)
        for ch in s1:
            sorted_s1[ord(ch) - ord('a')] += 1 
        for i in range(m - n + 1):
            tmp = s2[i: (i+n)]
            if i == 0:
                for ch in tmp:
                    sorted_s2[ord(ch) - ord('a')] += 1 
            else:
                sorted_s2[ord(s2[i-1]) - ord('a')] -= 1 
                sorted_s2[ord(tmp[-1]) - ord('a')] += 1 
            if sorted_s1 == sorted_s2:
                return True 
                
        return False
