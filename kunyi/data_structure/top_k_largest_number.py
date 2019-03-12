import heapq
class Solution:
    """
    @param nums: an integer array
    @param k: An integer
    @return: the top k largest numbers in array
    """
    def topk(self, nums, k):
        # heapsort nlogk
        heap = []
        for num in nums:
            if len(heap) == k and heap[0] < num:
                # heap[0] is the kth smallest item
                heapq.heappushpop(heap, num)
            elif len(heap) < k:
                heapq.heappush(heap, num)
         
        result = [] 
        for i in range(k):
            result.append(heapq.heappop(heap))
        return result[::-1]
