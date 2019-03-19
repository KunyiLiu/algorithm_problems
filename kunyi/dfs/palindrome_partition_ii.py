class Solution:
    """
    @param s: A string
    @return: An integer
    """
    def isPalidrome(self, s):
        n = len(s)
        palin = [[False] * n for i in range(n)]
        for i in range(n):
            palin[i][i] = True  # single word
            
        # two word
        for i in range(n-1):
            palin[i][i+1] = s[i] == s[i+1]
        
        # i is length 
        for i in range(2, n):
            # n-1 = n-i+i-1
            for j in range(0, n-i):
                palin[j][j+i] = palin[j+1][j+i-1] and s[j] == s[j+i]
                
        return palin  

    def minCut(self, s):
        #f[i] 表示前i个字母，最少可以被分割为多少个回文串
        #最后return f[n] - 1
        # have isPalidrome[n][n] table to mark s[i][j] is palidrom 
        # induction
        # f[i] min(f[i), f[j] + 1) if isPalidrome[j][i-1] is true
        if s is None or len(s) == 0:
            return 0 
        n = len(s)
        f = [i for i in range(n+1)]  # 0 ... n 
        palin_table = self.isPalidrome(s)
        for i in range(1, n+1):
            for j in range(0, i):
                if palin_table[j][i-1]:
                    f[i] = min(f[i], f[j]+1)
                    
        return f[n] - 1
