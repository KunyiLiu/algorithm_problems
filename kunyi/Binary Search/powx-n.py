class Solution:
    """
    @param x: the base number
    @param n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        # consider negative 
        if n == 0:
            return 1 
        ans = 1 
        if n < 0:
            x = 1/x
            n = -n
        while n > 0:
            if n % 2 == 1:
                ans = round(ans * x, 6) 
                
            x = round(x * x, 6) 
            n = n // 2
            
        return ans
