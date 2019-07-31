"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        d = {}
        for emp in employees:
            d[emp.id] = emp
        cur_emp = d[id]
        importance = self.bfs(cur_emp, d) 
        return importance 
    
    def  bfs(self, emp, d):
        visited = set()
        visited.add(emp.id)
        from collections import deque
        queue = deque([])
        for sub in emp.subordinates:
            queue.append(sub)
        importance = emp.importance
        while queue:
            cur_id = queue.popleft()
            cur_emp = d[cur_id]
            importance += cur_emp.importance
            for sub in cur_emp.subordinates:
                if sub not in visited:
                    queue.append(sub)
                    visited.add(sub)
        return importance
                    
                    
'''
Success
Details 
Runtime: 168 ms, faster than 100.00% of Python3 online submissions for Employee Importance.
Memory Usage: 14.9 MB, less than 5.49% of Python3 online submissions for Employee Importance.
Next challenges: Nested List Weight Sum

Related Topics: Hash Table, Depth-first Search, Breadth-first Search
'''
        
