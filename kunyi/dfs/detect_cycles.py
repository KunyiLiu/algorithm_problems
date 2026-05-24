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
