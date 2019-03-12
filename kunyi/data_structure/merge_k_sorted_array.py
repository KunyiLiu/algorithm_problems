import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        # heapq records val, row, ind 
        # O(nlogk)
        heap = []
        result = []
        for i in range(len(arrays)):
            array = arrays[i]
            if len(array) > 0:
                heapq.heappush(heap, (array[0], i, 0))
        
        while heap:
            value, row, ind = heapq.heappop(heap)
            result.append(value)
            if ind + 1 < len(arrays[row]):
                heapq.heappush(heap, (arrays[row][ind + 1], row, ind + 1))
                
        return result 
