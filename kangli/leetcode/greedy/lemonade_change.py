class Solution:
    def lemonadeChange(self, bills):
        counts = {}
        if bills[0] != 5:
            return False
        for b in bills:
            if b == 5:
                counts[b] = 1 if b not in counts else counts[b]+1 
            if b == 10:
                if 5 not in counts:
                    return False
                else:
                    counts[5] -= 1 
                    counts[b] = 1 if b not in counts else counts[b]+1 
            if b == 20:
                if 10 not in counts: 
                    if counts[5] < 3:
                        return False
                    else:
                        counts[5] -= 3 
                else:
                    if counts[5] < 1:
                        return False
                    counts[10] -= 1
                    counts[5] -=1 
        return True


'''
Success
Details 
Runtime: 44 ms, faster than 92.57% of Python3 online submissions for Lemonade Change.
Memory Usage: 13.2 MB, less than 92.05% of Python3 online submissions for Lemonade Change.
Next challenges:
Jump Game II
Meeting Rooms II
Largest Values From Labels
Related Topics: Greedy
'''
