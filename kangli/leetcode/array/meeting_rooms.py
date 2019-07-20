class Solution:
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda x:x[1])
        for i in range(len(intervals)-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
        return True
        

'''
Success
Details 
Runtime: 44 ms, faster than 67.79% of Python3 online submissions for Meeting Rooms.
Memory Usage: 15.2 MB, less than 47.73% of Python3 online submissions for Meeting Rooms.
Next challenges: Merge Intervals, Meeting Rooms II

Related Topics: Sort
Similar Questions: Merge Intervals, Meeting Rooms II
'''
