class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        # factorization , O(n^2)
        fact = [1]
        for i in range(1, n + 1):
            fact.append(fact[-1]*i)
            
        eligible = [i+1 for i in range(n)]
        result = []
        for i in range(n):
            # digit th int in eligible
            digit = (k-1) // fact[n-i-1]
            result.append(str(eligible[digit]))
            eligible.remove(eligible[digit])
            k = (k-1) % fact[n-i-1] + 1 
            
        return ''.join(result)
