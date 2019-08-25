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
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        if intervals is None or len(intervals) == 0:
            return True
        intervals = sorted(intervals, key = lambda x: x.start)
        end = intervals[0].end
        for interval in intervals[1:]:
            if interval.start < end:
                return False
            end =  interval.end
        return True
