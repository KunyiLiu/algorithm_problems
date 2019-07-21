"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required
    """
    def minMeetingRooms(self, intervals):
        # use heap the record the largest end of each rooms 
        import heapq
        intervals = sorted(intervals, key=lambda x: x.start)
        heap = []
        for ind, interval in enumerate(intervals):
            if ind == 0:
                heapq.heappush(heap, interval.end)
            elif interval.start < heap[0]:
                heapq.heappush(heap, interval.end)
            else:
                # Pop and return the smallest item from the heap, and also push the new item
                heapq.heapreplace(heap, interval.end)
                
        return len(heap) 
