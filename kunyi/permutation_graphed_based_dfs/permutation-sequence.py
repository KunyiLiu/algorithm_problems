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
    
    
    
############### str list join ############
class Solution:
    """
    @param n: n
    @param k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        # factorization 
        digit = n
            
        result = []
        eligible = [i for i in range(n-digit+1, n+1)]
        # O(n)
        factorization = {0: 1}
        self.get_fact(n, factorization)
        while digit > 0:
            eligible_ind = (k - 1)// factorization[digit-1]  # 3, 4 -> 1
            result.append(str(eligible[eligible_ind]))
            eligible.remove(eligible[eligible_ind])
            k = (k - 1) % factorization[digit-1] + 1 
            digit -= 1 
            
        return ''.join(result)
        
    def get_fact(self, n, memo):
        if n in memo:
            return memo[n]
            
        memo[n] = n * self.get_fact(n-1, memo)
        
        return memo[n]
