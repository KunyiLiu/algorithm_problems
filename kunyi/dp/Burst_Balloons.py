##### reference: permutations ####

#### Brute Force ######

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # try use the permutation recursion + memo
        # use remaining keys (tuple) as the key of memo
        # Time/Space -> O(n^2 * 2^n)
        # The number of different path states equals the number of subsets of balloons.
        # subset: for each baloon, should it be present or removed
        nums = [1] + nums + [1]
        memo = {}

        def dfs(path):
            if len(path) == 2:
                return 0

            key = tuple(path)
            if key in memo:
                return memo[key]

            max_coin = 0
            for i in range(1, len(path) - 1):
                coins = path[i-1] * path[i] * path[i+1]
                coins += dfs(path[:i] + path[i+1:])
                max_coin = max(max_coin, coins)

            memo[key] = max_coin

            return max_coin

        return dfs(nums)

#####  Reverse Thinking, Burst Last ####

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # instead of choosing the first balloon to burst, 
        # choose the last balloon to burst in a subarray.
        # l .. i .. r, if i is the last to pop, consider 2 subarrays (l..i-1), (i+1,..r)
        # dp(l, r) = nums[l-1] * nums[i] * nums[r + 1] + dp(l, i -1) + dp(i + 1, r)
        # Time complexity: O(n^3), Space: O(n^2)
        nums = [1] + nums + [1]
        # memo
        dp = {}

        def dfs(l, r):
            if l > r:
                return 0
            
            if (l, r) in dp:
                return dp[(l,r)]

            max_coin = 0
            for i in range(l, r + 1):
                coins = nums[l-1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                max_coin = max(max_coin, coins)

            dp[(l, r)] = max_coin

            return max_coin

        return dfs(1, len(nums) - 2)


            
                




