class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Counter {1: 3, 2: 2, 3: 1} 
        # heapq, pop out the smallest one and keep the size as k, so input (count, key)
        # O(nlogk)
        import heapq
        from collections import Counter 
        nums_count = Counter(nums)
        heap = []
        for num, count in nums_count.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)
                
        return [j for i, j in heap][::-1]
        
 ######################
 class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @re/turn: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Counter {1: 3, 2: 2, 3: 1} 
        # bucket sort, convert counter hashtable to a list of (k, v) tuples reversely sorted based on v
        # O(nlogn)
        from collections import Counter 
        nums_count = Counter(nums)
        freq_list = sorted(nums_count.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(freq_list[i][0])
            
        return result 
        
#################### bucket sort ####################
class Solution:
    """
    @param nums: the given array
    @param k: the given k
    @return: the k most frequent elements
    """
    def topKFrequent(self, nums, k):
        # Counter {1: 3, 2: 2, 3: 1} 
        # bucket sort
        # O(n)
        from collections import Counter, defaultdict
        nums_count = Counter(nums)
        freq_count = defaultdict(list)
        
        for num, count in nums_count.items():
            freq_count[count].append(num)
         
        result = [] 
        for i in range(len(nums), -1, -1):
            if i in freq_count:
                result.extend(freq_count[i])
            
        return result[:k] 
        
     
