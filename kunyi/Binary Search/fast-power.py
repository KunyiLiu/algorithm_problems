############ recursion 1.    #############
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # something like fabonacci (recursion + hash table for memoization)
        # memo not much help here 
        # cornor case
        memo_hash = {0: 1%b, 1: a%b}
        result = self.helper(a, b, n, memo_hash)
        return result
        
    def helper(self, a, b, n, memo_hash):
        # exit n == 0 or 1 in memo_hash
        if n in memo_hash:
            return memo_hash[n]
        
        if n % 2 != 0:
            tmp_result = self.helper(a, b, n//2, memo_hash)
            result = (tmp_result * tmp_result * memo_hash[1]) % b 
        else:
            tmp_result = self.helper(a, b, n//2, memo_hash)
            result = (tmp_result * tmp_result) % b 
            
        memo_hash[n] = result
        return result

######## Recursion 2. ###############
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b
            
        if n == 1:
            return a % b
            
        # a^n = (a^n/2) ^ 2
        power = self.fastPower(a, b, n // 2)
        power = (power * power) % b
        
        # 如果 n 是奇数，还需要多乘以一个 a，因为 n // 2 是整除
        if n % 2 == 1:
            power = (power * a) % b
            
        return power

######## Iteration ###########
class Solution:
    """
    @param a, b, n: 32bit integers
    @return: An integer
    """
    def fastPower(self, a, b, n):
        # a ^ n % b
        # 比如 n=5,可以看做 a^(101)2 % b （5的二进制是101）
        # 拆开也就是 [a^(100)2 * a&(1)2] % b
        # 因此相当于我们把 n 做二进制转换，碰到 1 的时候，称一下对应的 a 的幂次
        # 而 a 的幂次我们只需要知道 a^1, a^(10)2, a^(100)2 ... 也就是 a^1, a^2, a^4 ...
        # 因此不断的把 a = a * a 就可以了
        # 中间计算的时候，随时可以 % b 避免 overflow 其不影响结果，这是 % 运算的特性。
        ans = 1
        while n > 0:
            if n % 2 == 1:
                ans = (ans * a) % b
            a = a * a % b
            n = n // 2
        return ans % b
