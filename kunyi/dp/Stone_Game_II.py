class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        # create dp[alice][left][M], M start from 1. 
        # dp[alice][0][1] = max(dp[bob][1][1] + piles[0], dp[bob][2][2] + piles[0 - 1])
        # Both players play optimally -> Alice try to max the result, while Bob try to minimize the result

        # Time complexity: O(n^3) 
        dp = {}

        def dfs(alice, left, M):
            if left == len(piles):
                return 0

            if (alice, left, M) in dp:
                return dp[(alice, left, M)]

            # if bob turn, try to minimize the result
            result = 0 if alice else float("inf")
            total = 0
            # one turn -> result for alice
            for i in range(1, 2 * M + 1):
                if i + left > len(piles):
                    break

                total += piles[i + left - 1]
                if alice:
                    # next turn is Bob
                    result = max(result, total + dfs(False, i + left, max(M, i)))
                else:
                    # next turn is Alice
                    result = min(result, dfs(True, i + left, max(M, i)))

            dp[(alice, left, M)] = result

            return result

        return dfs(True, 0, 1)

        
