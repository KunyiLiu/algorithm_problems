########## dfs + memo#####
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        n = len(nums)

        memo = [[None] * (target + 1) for _ in range(n)]

        def dfs(i, remain):
            if remain == 0:
                return True
            if i == n or remain < 0:
                return False

            if memo[i][remain] is not None:
                return memo[i][remain]

            # Decision: take OR skip
            take = dfs(i + 1, remain - nums[i])
            skip = dfs(i + 1, remain)

            memo[i][remain] = take or skip
            return memo[i][remain]

        return dfs(0, target)


##### bottom up ####
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        Determine whether the array can be partitioned into two subsets
        with equal sum.

        This is a classic 0/1 knapsack (subset sum) problem.

        Idea:
        - If total sum is odd → impossible.
        - Otherwise, we need to check whether there exists a subset
          whose sum equals total // 2.

        State Definition:
            dp[t] = True  if we can form sum t using some subset
                           of the processed numbers.
                    False otherwise.

        Initialization:
            dp[0] = True  (empty subset always forms sum 0)

        Transition:
            For each number `num`,
            we update dp[t] as:

                dp[t] |= dp[t - num]

            Meaning:
            If we could previously form (t - num),
            then by taking `num`, we can now form t.

        Important:
            We iterate t from target down to num (reverse order).

            Why reverse?
            - To ensure each number is used at most once (0/1 constraint).
            - If we iterate forward, we would reuse the same number
              multiple times in the same iteration (which would turn
              it into an unbounded knapsack problem).

        Time Complexity:  O(n * target)
        Space Complexity: O(target)
        """

        total = sum(nums)
        if total % 2:
            return False

        target = total // 2

        # dp[t] indicates whether sum t is achievable
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # iterate backward to prevent reusing the same number
            for t in range(target, num - 1, -1):
                dp[t] |= dp[t - num]

        return dp[target]
