"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # return it as a new sorted list
        # sorted([2, 5, 4], cmp = cmp)
        # O((n+m)log(n+m))
        merge_list = sorted(list1 + list2, key = lambda x: x.start)
        result = []
        for interval in merge_list:
            if len(result) == 0 or result[-1].end < interval.start:
                result.append(interval)
            else:
                result[-1].end = max(result[-1].end, interval.end)
                
        return result 
