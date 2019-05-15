##############     heapq ########################

import heapq

class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """

    def mergekSortedArrays(self, arrays):
        # heapq records val, ind 
        # maximumly put k elements to heap
        # O(N log k)
        heap = []
        result = []
        for i in range(len(arrays)):
            array = arrays[i]
            if len(array) > 0:
                heapq.heappush(heap, (array[0], i, 0))
        
        while heap:
            value, row, ind = heapq.heappop(heap)
            # the smallest of the three first elements of the first list 
            # must be the smallest one 
            result.append(value)
            if ind + 1 < len(arrays[row]):
                heapq.heappush(heap, (arrays[row][ind + 1], row, ind + 1))
                
        return result
        
############  DQ & Recursion   ###################
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # divide & conquer (top-down)
        # T(k) = 2T(k/2) + (n) = nlogk
        return self.merge_array_list(arrays, 0, len(arrays) - 1)
        
    def merge_array_list(self, arrays, start, end):
        # recursion
        if start == end:
            return arrays[start]
            
        mid = start + (end - start) // 2 
        left_result = self.merge_array_list(arrays, start, mid)
        right_result = self.merge_array_list(arrays, mid + 1, end)
        
        return self.merge_two_arrays(left_result, right_result)
        
    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array
        
###########      buttom up ######################
class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        # buttom up 
        # O(k(n))
        while len(arrays) > 1:
            array = self.merge_two_arrays(arrays[-2], arrays[-1])
            del arrays[-2]
            del arrays[-1]
            arrays.append(array)
            
        return arrays[0]
        
    def merge_two_arrays(self, arr1, arr2):
        i, j = 0, 0
        array = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                array.append(arr1[i])
                i += 1
            else:
                array.append(arr2[j])
                j += 1
        while i < len(arr1):
            array.append(arr1[i])
            i += 1
        while j < len(arr2):
            array.append(arr2[j])
            j += 1
        return array
