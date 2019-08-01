class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) <= 1:
            return intervals
        intervals = sorted(intervals)
        last, res = intervals[0], []
        
        for interval in intervals:
            if len(res) == 0:
                res.append(interval)
            else:
                if last[1] >= interval[0]:
                    last[1] = max(interval[1], last[1])
                else:
                    res.append(interval)
                    last = interval
        return res
        

'''
Success
Details 
Runtime: 120 ms, faster than 11.08% of Python3 online submissions for Merge Intervals.
Memory Usage: 15.9 MB, less than 5.10% of Python3 online submissions for Merge Intervals.
Next challenges: Insert Interval, Meeting Rooms II, Teemo Attacking, Add Bold Tag in String, Range Module, 
Employee Free Time, Partition Labels
'''
