class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # sort the intervals as well as queries,
        # add interval to the minheap if start <= q;
        # pop those intervals if it is far left (not needed for the increasing q later)
        # get the smallest length interval from the top of minheap
        # Time: O(nlogn + qlogq), Space: O(n + m)
        import heapq
        result = [-1] * len(queries)
        intervals.sort()
        i = 0
        minheap = []

        for j, q in sorted(enumerate(queries), key = lambda x: (x[1], x[0])):
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(minheap, (r - l + 1, r))
                i += 1

            while minheap and minheap[0][1] < q:
                heapq.heappop(minheap)

            if minheap:
                result[j] = minheap[0][0]

        return result


        
