class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        last_end = None
        count = 0
        for ind, interval in enumerate(intervals):
            if ind == 0:
                last_end = interval[1]
            elif ind > 0 and interval[0] < last_end:
                count += 1 
                # remove the interval with largest end after comparing the current and last interval
                last_end = min(last_end, interval[1])
            else:
                last_end = interval[1]          
                
        return count
            
