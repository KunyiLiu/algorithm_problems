class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        import heapq 
        res, freq = [], Counter(nums)
        heap_array = [(-val, integer) for integer, val in freq.items()]
        heapq.heapify(heap_array)
        while k > 0:
            res.append(heapq.heappop(heap_array)[1])
            k -= 1 
        return res 
        

'''
Success
Details 
Runtime: 120 ms, faster than 63.74% of Python3 online submissions for Top K Frequent Elements.
Memory Usage: 18.5 MB, less than 6.41% of Python3 online submissions for Top K Frequent Elements.
Next challenges: Word Frequency, Split Array into Consecutive Subsequences, Top K Frequent Words

Related Topics: Hash Table, Heap
Word Frequency, Kth Largest Element in an Array, Sort Characters By Frequency, Split Array into Consecutive Subsequences, 
Top K Frequent Words, K Closest Points to Origin
'''
