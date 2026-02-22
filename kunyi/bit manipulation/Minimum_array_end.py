class Solution:
    def minEnd(self, n: int, x: int) -> int:
        # x is the common prefix, go larger
        # until the total number meet n.
        # two pointer algorithm: put the n - 1 integers to the remaining bits if not 1
        # Time: O(logn + logx). Fill in n - 1 bits to the 0 "holes" of x
        
        if n == 1:
            return x

        last_elem = x
        i_x = 1 # 1, 10, 100
        i_n = 1 

        while i_n <= n - 1:
            # if the ith bit of x is 0, which means I can input 1 to it
            if i_x & x == 0:
                # if the ith bit of n is 1, I can fill in 1 to i_xth bit
                if i_n & (n - 1):
                    last_elem |= i_x
                
                i_n <<= 1 

            i_x <<= 1

        return last_elem
