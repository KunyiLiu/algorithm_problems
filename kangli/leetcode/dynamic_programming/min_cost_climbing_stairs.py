class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        cache = [0 for i in range(len(cost) + 1)]
        cache[0], cache[1] = cost[0], cost[1]
        for i in range(2, len(cost)):
            cache[i] = cost[i] + min(cache[i - 2], cache[i - 1])
        return min(cache[n - 2], cache[n - 1])


'''
Success
Details
Runtime: 48 ms, faster than 32.85% of Python online submissions for Min Cost Climbing Stairs.
Memory Usage: 11.7 MB, less than 5.71% of Python online submissions for Min Cost Climbing Stairs.
Next challenges:
Count Numbers with Unique Digits
Freedom Trail
Maximum Length of Repeated Subarray

Related Topics: Dynamic Programming
Similar Questions: Climbing Stairs
Hint 1: Say f[i] is the final cost to climb to the top from step i. Then f[i] = cost[i] + min(f[i+1], f[i+2]).
'''
