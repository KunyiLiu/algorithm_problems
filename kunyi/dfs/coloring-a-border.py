######## BFS ########
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        # dfs/bfs find connected component in 4 directions 
        if grid is None or len(grid) == 0:
            return 
        m, n = len(grid), len(grid[0])
        queue = [(r0, c0)]
        tag_color = grid[r0][c0]
        visited_components,  border = set([(r0, c0)]), set()
        
        delta_X = [1, -1, 0, 0]
        delta_Y = [0, 0, 1, -1]
        while len(queue) > 0:
            x, y = queue.pop(0)
            for i in range(4):
                new_x, new_y = x + delta_X[i], y + delta_Y[i]
                if 0 <= new_x < m and 0 <= new_y < n and grid[new_x][new_y] == tag_color:
                    if (new_x, new_y) not in visited_components:
                        queue.append((new_x, new_y))
                        visited_components.add((new_x, new_y))
                else:
                    border.add((x, y))
                    # disobey grid[new_x][new_y] == tag_color -> 4-directionally adjacent to a square not in the component,
                   # disobey 0 <= new_x < m and 0 <= new_y < n -> on the boundary of the grid 
                    
        for x, y in border:
            grid[x][y] = color
        return grid

########### DFS #########
class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        """
        set up a dfs helper function,
        start from (r0, c0), find and color all the border nodes 
        """
        if grid is None or len(grid) == 0:
            return grid 
        
        m, n = len(grid), len(grid[0])
        seen = set()
        def dfs(x, y, seen):
            # will finally go to the first row, col, break this road
            if (x, y) in seen:
                return False  

            # out of grid or not in the component
            if not(0<= x < m and 0<= y < n and grid[x][y] == grid[r0][c0]):
                return True
            
            # location
            seen.add((x,y))
            is_left = dfs(x-1, y, seen)
            is_right = dfs(x+1, y, seen)
            is_up = dfs(x, y-1, seen)
            is_down = dfs(x, y+1, seen)
            if any([is_left, is_right, is_up, is_down]):
                grid[x][y] = color 
                
            return False 
        
        dfs(r0, c0, seen)
        return grid
            
        
