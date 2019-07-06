class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Counter {1: 3, 2: 2, 3: 1} 
        # bucket sort, convert counter hashtable to a list of (k, v) tuples reversely sorted based on v
        from collections import Counter 
        nums_count = Counter(nums)
        counts = [(k,v) for k, v in nums_count.items()]
        freq_list = self.quick_sort(counts, 0, len(counts) - 1, k - 1)
            
        return [_[0] for _ in freq_list]
        
    def quick_sort(self, counts, left, right, k):
        pivot = counts[left]
        l, r = left, right
        while l <= r:
            while l <= r and counts[l][1] > pivot[1]:
                l += 1
            while l <= r and counts[r][1] < pivot[1]:
                r -= 1
            
            if l <= r:
                counts[l], counts[r] = counts[r], counts[l]
                l += 1 
                r -= 1 
        
        # elements before l, > pivot
        if l - 1 == k:
            return counts[:l]
        elif l - 1 < k:
            return self.quick_sort(counts, l, right, k)
        else:
            return self.quick_sort(counts, left, l - 1, k)
