class Solution:
    def dailyTemperatures(self, T):
        ans = [0] * len(T)
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans

'''
Success
Details
Runtime: 288 ms, faster than 98.16% of Python3 online submissions for Daily Temperatures.
Memory Usage: 16.8 MB, less than 29.03% of Python3 online submissions for Daily Temperatures.
Next challenges:
Next Greater Element I

Related Topics: Hash Table, Stack
Similar Questions: Next Greater Element I
Hint 1: If the temperature is say, 70 today, then in the future a warmer temperature must be
 either 71, 72, 73, ..., 99, or 100. We could remember when all of them occur next.
'''
