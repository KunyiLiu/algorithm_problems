class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if not trust:
            return N
        in_degree, out_degree = {}, {}
        for t in trust:
            in_degree[t[1]] = 1 if t[1] not in in_degree else in_degree[t[1]]+1
            out_degree[t[0]] = 1
        for k, v in in_degree.items():
            if v == N-1 and k not in out_degree:
                return k
        return -1
        
        
'''
Success
Details 
Runtime: 848 ms, faster than 57.85% of Python3 online submissions for Find the Town Judge.
Memory Usage: 18.3 MB, less than 10.00% of Python3 online submissions for Find the Town Judge.
Next challenges: Find the Celebrity

Related Topics: Graph (in-degree, out-degree concept)
Similar Questions: Find the Celebrity
'''
