class Solution:
    def frequencySort(self, s: str):
        from collections import Counter, defaultdict
        counts = Counter(s)
        freqs = defaultdict(list)
        res = []
        for k, v in counts.items():
            freqs[v].append(k)    
        max_freq = len(s) 
        while max_freq > 0:
            if max_freq in freqs:
                for c in freqs[max_freq]:
                    res.append(c*max_freq)
            max_freq -= 1 
        return "".join(res)
 
 '''
Success
Details 
Runtime: 52 ms, faster than 59.95% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 13.7 MB, less than 71.06% of Python3 online submissions for Sort Characters By Frequency.
Next challenges:
Maximal Rectangle
Happy Number
Rearrange String k Distance Apart

Related Topics: Hash Table, Heap
Similar Questions: Top K Frequent Elements, First Unique Character in a String
 '''
