"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: interval list.
    @return: A new interval list.
    """
    def merge(self, intervals):
        # sorting nlog(n)
        intervals = sorted(intervals, key=lambda x: x.start)
        result = []
        for i in range(len(intervals)):
            if i == 0 or result[-1].end < intervals[i].start:
                result.append(intervals[i])
            else:
                result[-1].end = max(result[-1].end, intervals[i].end)
                
        return result 
