### Greedy, O(n) ####
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Greedy, when scanning left to right, there could be 3 states
        # 1. new interval on the left (non-overlapping), 2. on the right (non-overlapping, but could overlap with later intervals)
        # 3. overlap with current interval, expand new interval

        result = []
        for i, interval in enumerate(intervals):
            if newInterval[1] < interval[0]:
                result.append(newInterval)
                return result + intervals[i:]
            elif newInterval[0] > interval[1]:
                result.append(interval)
            else:
                newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

        result.append(newInterval)
        return result

# basic, reference merge intervals ###

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #  reference: merge intervals -> stack 
        # traverse the intervals and append it to the stack result until 
        # the start of new_interval < end of last elem of stack.
        # pop the interval from stack, 
        new_intervals = intervals + [newInterval]
        new_intervals.sort(key = lambda x: (x[0], x[1]))
        result = []

        for interval in new_intervals:
            new_start, new_end = interval[0], interval[1]
            if not result or result[-1][1] < new_start:
                result.append(interval)
            else:
                cur_start, cur_end = result.pop()
                result.append([min(new_start, cur_start), max(new_end, cur_end)])

        return result
