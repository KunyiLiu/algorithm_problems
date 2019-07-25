class Solution:
    """
    @param n: a positive integer represented by string
    @return:  the closest integer which is a palindrome
    """
    def nearestPalindromic(self, n):
        # Write your code here
        a , res = int(n) , 0    	#字符串转化为整数
        half = int(10**(len(n) // 2))
        b = a // half * half
        candidates = [b , b - (half // 10 if (half > 1) else 1 ), b + half]	#构造三个数字
        for cand in candidates :		#对3个数字每次进行构造回文串
            cand  = self.mirroring(cand)
            if cand == a:
                continue
            if abs(res - a) > abs(cand - a) or (abs(res - a) == abs(cand - a) and cand < res) :	#比较结果
                res = cand
        return str(res)
    
    def mirroring(self, n) :	#传入数字构造回文串
        m , x , half , i = 0 , n , 1 , 0
        while x :
            m = m * 10 + x % 10
            x //=  10
        half = int(10**(len(str(n)) // 2))
        return n // half * half + m % half
