class Solution:
    def myPow(self, x: float, n: int) -> float:
        #  x^13, 13 = 1101, x ^ (8 + 4 + 1) = x^8 * x ^ 4 * x
        #                                x
        # Time complexity: O(logn)
        if n == 0:
            return 1.0

        power = n if n > 0 else -n
        result = 1 
        
        while power:
            # odd, meaning bit is 1
            if power & 1:
                result *= x
            x *= x 
            # divide by 2
            power >>= 1

        return result if n > 0 else 1/result

        
