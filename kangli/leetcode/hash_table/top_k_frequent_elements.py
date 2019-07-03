from collections import Counter, defaultdict


class Solution:
    def topKFrequent(self, nums, k):
        counts = Counter(nums)
        freq = defaultdict(list)
        res = []
        for key, v in counts.items():
            freq[v].append(key)
        for i in range(len(nums), -1, -1):
            if i in freq:
                res.extend(freq[i])
        return res[0:k]

'''
Related Topics: Hash Table, Heap
Similar Questions: Word Frequency, Kth Largest Element in an Array, Sort Characters By Frequency
Split Array into Consecutive Subsequences, Top K Frequent Words, K Closest Points to Origin

Success
Details
Runtime: 44 ms, faster than 91.47% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 15.8 MB, less than 65.17% of Python3 online submissions for Top K Frequent Elements.
Next challenges:
Word Frequency
Kth Largest Element in an Array
Sort Characters By Frequency
Split Array into Consecutive Subsequences
Top K Frequent Words
K Closest Points to Origin
'''
