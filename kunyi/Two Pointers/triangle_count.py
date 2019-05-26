class Solution:
    """
    @param S: A list of integers
    @return: An integer
    """
    def triangleCount(self, S):
        # write your code here
        S = sorted(S)
        result = 0 
        for i in range(len(S) - 1, 1, -1):
            target = S[i]
            start, end = 0, i - 1 
            while start < end:
                if S[start] + S[end] > target:
                    result += (end - start)
                    end -= 1
                else:
                    start += 1 
                    
        return result
