class Solution:
    def kClosest(self, points, K):
        heap=[]
        for a,b in points:
            d=a*a+b*b
            heapq.heappush(heap,(-d,a,b)) # -d is for inverse value of data ( pop minimum distance instead of maximum )
            if len(heap)>K: # Keep length of heap in size K
                heapq.heappop(heap)
        return [[b,c] for a,b,c in heap]


'''
Success
Details 
Runtime: 744 ms, faster than 72.82% of Python3 online submissions for K Closest Points to Origin.
Memory Usage: 20.1 MB, less than 5.24% of Python3 online submissions for K Closest Points to Origin.
Next challenges:Kth Largest Element in an Array, Top K Frequent Elements, Top K Frequent Words

Related Topics: Divide and Conquer, Heap, Sort
'''
