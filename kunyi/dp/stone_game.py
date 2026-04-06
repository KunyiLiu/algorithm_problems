class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Both players play optimally -> not playing in a greedy way.
        # with each number of piles and total odd number, there has to be a winner. So the first player can win.
        return True


###  Time complexity: O(n*n), DF + memo ###

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}

        def dfs(alice, left, right):
            if left > right:
                return 0

            if (alice, left, right) in dp:
                return dp[(alice, left, right)]

            # if bob turn, try to minimize the result
            result = 0 if alice else float("inf")
            # one turn -> result for alice
            if alice:
                # next turn is Bob
                result = max(result, piles[left] + dfs(False, left + 1, right), piles[right] + dfs(False, left, right - 1))
            else:
                # next turn is Alice
                result = min(result, dfs(True, left + 1, right), dfs(True, left, right - 1))

            dp[(alice, left, right)] = result

            return result

        alice_best = dfs(True, 0, len(piles) - 1)
        return alice_best > sum(piles) // 2
