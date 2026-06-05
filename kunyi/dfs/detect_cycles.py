# Kahn algorithm



# DFS + 3 color state 

    def _check_cycles(self) -> None:
        # Track nodes fully processed to avoid redundant work across different roots
        visited = set()
        
        for task in self._tasks.values():
            if task.name not in visited:
                # We track the current recursion path using standard DFS
                rec_stack = set()
                self._dfs_check(task, visited, rec_stack)

    def _dfs_check(self, task: Task, visited: set, rec_stack: set) -> None:
        # Add to the current path
        rec_stack.add(task.name)
        
        for dep_name in task.depends_on:
            # If a dependency is already in the current recursion stack, we found a loop!
            if dep_name in rec_stack:
                raise CycleError(f"cycle detected involving: {task.name} -> {dep_name}")
            
            # Only recurse if we haven't fully explored this dependency before
            if dep_name not in visited:
                dep_task = self._tasks[dep_name]
                self._dfs_check(dep_task, visited, rec_stack)



# golden example

from typing import List, Dict

class DirectedGraphCycleDetector:
    def has_cycle(self, num_nodes: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build the adjacency list
        adj_list = {i: [] for i in range(num_nodes)}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            
        # Step 2: Initialize states for all nodes (0 = Unvisited)
        state = {i: 0 for i in range(num_nodes)}
        
        # Step 3: Helper function for DFS
        def dfs(node: int) -> bool:
            # If we hit a node currently being visited, we found a cycle!
            if state[node] == 1:
                return True
            # If the node is already fully processed, no need to visit again
            if state[node] == 2:
                return False
            
            # Mark the node as "Visiting" (push to recursion stack)
            state[node] = 1
            
            # Recurse for all neighbors
            for neighbor in adj_list[node]:
                if dfs(neighbor):
                    return True # Cycle detected downstream
                    
            # Mark the node as "Fully Processed" (pop from recursion stack)
            state[node] = 2
            return False

        # Step 4: Run DFS from every node to cover disconnected components
        for current_node in range(num_nodes):
            if state[current_node] == 0:
                if dfs(current_node):
                    return True # Cycle found somewhere in the graph
                    
        return False # Graph is a valid DAG (No cycles)
