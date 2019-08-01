
class Solution:
    def findRedundantConnection(self, edges):
        root = [0]*(len(edges)+1)
        
    
        def find(x):
            if root[x] == 0:
                return x
            root[x] = find(root[x])
            return root[x]
    
        def union_with_check(x, y):
            rx, ry = find(x), find(y)
            if rx == ry:
                return False
            root[rx] = ry
            return True
        
        for x, y in edges:
            if not union_with_check(x, y):
                return [x, y]
        return []
        

'''
Success
Details 
Runtime: 64 ms, faster than 81.17% of Python3 online submissions for Redundant Connection.
Memory Usage: 14.2 MB, less than 12.59% of Python3 online submissions for Redundant Connection.
Next challenges: Redundant Connection II, Accounts Merge

Related Topics: Tree, Union Find, Graph
Similar Questions: Redundant Connection II, Accounts Merge
'''
    
