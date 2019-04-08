#top down dp

class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        cache = [0]*(n+1)
        cache[1], cache[2] = 1, 2
        self.climb(n, cache)
        return cache[-1]

    def climb(self, n, cache):
        if cache[n] != 0:
            return cache[n]
        else:
            cache[n] = self.climb(n-1, cache) + self.climb(n-2, cache)
            return cache[n]

''''
Details 
Runtime: 20 ms, faster than 67.61% of Python online submissions for Climbing Stairs.
Memory Usage: 11.8 MB, less than 5.07% of Python online submissions for Climbing Stairs.
Next challenges:
Min Cost Climbing Stairs
Fibonacci Number

Related Topics: Dynamic Programming
Similar Questions: Min Cost Climbing Stairs
Easy
Fibonacci Number
Easy
Hint 1: To reach nth step, what could have been your previous steps? (Think about the step sizes)
'''


''' buggy code with fixes
class Solution(object):
    def climbStairs(self, n):
        if n == 1: #forgot edge case again...
            return 1
        cache = [0]*(n+1)
        cache[1], cache[2] = 1, 2
        self.climb(n, cache)
        return cache[-1]

    def climb(self, n, cache):
        if cache[n] != 0:
            return cache[n]
        else:
            cache[n] = self.climb(n-1, cache) + self.climb(n-2, cache)
            return cache[n] #needed this! otherwise nonetype + int error
s = Solution()
s.climbStairs(5)
'''


#recursive solution, TLE
class Solution(object):
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        else:
            return self.climbStairs(n-2) + self.climbStairs(n-1)

