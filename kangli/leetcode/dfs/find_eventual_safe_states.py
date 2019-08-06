class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        
        def dfs(graph, node, visited):
            if node in visited:
                return False
            else:
                visited.add(node)
            for neighbor in graph[node]:
                if neighbor in res:
                    continue
                if not dfs(graph, neighbor, visited):
                    return False
                visited.remove(neighbor)
            res.add(node)
            return True
        
        res = set()
        for n in range(len(graph)):
            dfs(graph, n, set())
            
        return sorted(list(res)) 


'''
Success
Details 
Runtime: 1236 ms, faster than 5.68% of Python3 online submissions for Find Eventual Safe States.
Memory Usage: 20.9 MB, less than 20.00% of Python3 online submissions for Find Eventual Safe States.
Next challenges: Construct Binary Tree from Inorder and Postorder Traversal, Flatten a Multilevel Doubly Linked List

Related Topics: Depth-first Search, Graph
'''
