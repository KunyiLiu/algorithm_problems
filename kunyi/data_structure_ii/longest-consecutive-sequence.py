class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """
    def longestConsecutive(self, num):
        # Question: is the list deduplicated? Assume no
        from collections import Counter
        hash_table = Counter()
        result = 0
        for i in num:
            hash_table[i] += 1 
        for i in num:
            tmp = 1
            if hash_table[i] < 0:
                continue
            l, r = i - 1, i + 1
            print hash_table
            while hash_table[l] > 0:
                tmp += 1 
                del hash_table[l]
                l -= 1
            while hash_table[r] > 0:
                tmp += 1 
                del hash_table[r]
                r += 1
            result = tmp if tmp > result else result
        return result
