class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        # have a person indregree = n-1, outdegree = 0 
        inds, outs = {}, {}
        for k, v in trust:
            if k not in outs:
                outs[k] = 0 
            outs[k] += 1 
            if v not in inds:
                inds[v] = 0
            inds[v] += 1 
            
        for i in range(1, N+1):
            if inds.get(i, 0) == N-1 and outs.get(i, 0) == 0:
                return i 
            
        return -1
