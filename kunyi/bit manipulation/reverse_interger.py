class Solution:
    def reverse(self, x: int) -> int:
      # Notice: 1 << 31 - 1 = 1 << (31 - 1)
        if x < -(1 << 31) or x > (1 << 31) - 1:
            return 0 
            
        sign = -1 if x < 0 else 1
        x *= sign
        
        rev = 0
        while x:
            rev = rev * 10 + x % 10
            x //= 10

        rev *= sign

        return rev if -(1 << 31) <= rev <= (1 << 31) - 1 else 0
