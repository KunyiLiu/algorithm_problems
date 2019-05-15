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

    
   #########  faster  #########
class Solution:
    """
    @param list1: one of the given list
    @param list2: another list
    @return: the new sorted list of interval
    """
    def mergeTwoInterval(self, list1, list2):
        # O(m + n)
        result = []
        i, j = 0, 0 
        while i < len(list1) and j < len(list2):
            if list1[i].start < list2[j].start:
                self.push_back(result, list1[i])
                i += 1 
            else:
                self.push_back(result, list2[j])
                j += 1 
                
        while i < len(list1):
            self.push_back(result, list1[i])
            i += 1 
            
        while j < len(list2):
            self.push_back(result, list2[j])
            j += 1
            
        return result 
        
    def push_back(self, result, element):
        if len(result) == 0 or result[-1].end < element.start:
            result.append(element)
        else:
            result[-1].end = max(result[-1].end, element.end)
            
        return 
