class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    def countOfSmallerNumber(self, A, queries):
        # m - A.length, n - queries.length
        # mlogm + nlogm
        sorted_A = sorted(A)
        result = []
        for q in queries:
            result.append(self.binary_search(sorted_A, q))
            
        return result 
        
    def binary_search(self, array, elem):
        if len(array) == 0:
            return 0
        start, end = 0, len(array) - 1 
        while start + 1 < end:
            mid = start + (end - start) // 2 
            if array[mid] >= elem:
                end = mid 
            else:
                start = mid

        if array[start] >= elem:
            return start
        if array[end] >= elem:
            return end
