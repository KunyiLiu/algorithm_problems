class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter, defaultdict
        char_counts = Counter(s)
        reverse_d = defaultdict(list)
        for c in char_counts:
            reverse_d[char_counts[c]].append(c)
        i = len(s)
        res = []
        while i > 0:
            if i in reverse_d:
                for c in reverse_d[i]:
                    res.append(c*i)
            i -= 1
        return "".join(res) 
                    
       
''' 
Runtime: 56 ms, faster than 49.51% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 14.9 MB, less than 15.22% of Python3 online submissions for Sort Characters By Frequency.
Next challenges:Top K Frequent Elements, First Unique Character in a String

Related Topics: Hash Table, Heap
'''
