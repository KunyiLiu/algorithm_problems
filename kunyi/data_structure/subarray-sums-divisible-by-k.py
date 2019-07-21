########## TLE O(n^2) ########
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # cur_sum = sum([0...i])
        ans = 0 
        cur_sum = 0 
        for i, num in enumerate(A):
            cur_sum += num 
            if cur_sum % K == 0:
                ans += 1 

            tmp_sum = cur_sum
            for j in range(i):
                tmp_sum -= A[j]
                if tmp_sum % K == 0:
                    ans += 1 
                        
        return ans
        
 ##### hash_table[i] = prefix_modulo #######
 ##### counter[prefix_modulo] = count, C(2, count) ####
 class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        # cur_sum = sum([0...i])
        from collections import Counter
        prefix_modulo = [0]
        for num in A:
            prefix_modulo.append((prefix_modulo[-1] + num) % K)
        
        modulo_count = Counter(prefix_modulo)
        return sum([v*(v-1)//2 for k, v in modulo_count.items()])
