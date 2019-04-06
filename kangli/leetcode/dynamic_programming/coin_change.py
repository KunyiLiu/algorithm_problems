class Solution(object):
    def coinChange(self, coins, amount):
        cache = [amount+1] * (amount+1)
        cache[0] = 0
        for i in range(1, amount+1):
            for c in coins:
                if i >= c:
                    cache[i] = min(cache[i], cache[i-c] + 1)
        if cache[amount] == amount+1:
            return -1
        return cache[amount]

'''
Success
Details 
Runtime: 1068 ms, faster than 53.33% of Python online submissions for Coin Change.
Memory Usage: 12 MB, less than 23.12% of Python online submissions for Coin Change.
Next challenges:
Minimum Cost For Tickets

Related Topics: Dynamic Programming
Similar Questions: Minimum Cost For Tickets
'''
