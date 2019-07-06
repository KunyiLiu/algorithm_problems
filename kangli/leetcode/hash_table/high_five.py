from collections import defaultdict


class Solution:
    def highFive(self, items):
        d, res = defaultdict(list), []
        for item in items:
            s_id = item[0]
            score = item[1]
            d[s_id].append(score)

        for s_id, scores in d.items():
            top_five_avg = self.top_five_avg(scores)
            res.append([s_id, top_five_avg])

        return res


'''
Success
Details
Runtime: 44 ms, faster than 48.37% of Python3 online submissions for High Five.
Memory Usage: 13.3 MB, less than 75.00% of Python3 online submissions for High Five.
Next challenges:
Line Reflection
Can Place Flowers
Maximum Swap

Related Topics: Array, Hash Table, Sort
Hints: 1) How can we solve the problem if we have just one student?
2) Given an student sort their grades and get the top 5 average.
3) Generalize the idea to do it for many students.
'''
