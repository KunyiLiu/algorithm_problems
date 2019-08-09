######### bfs time: O(n), space: O(n) ######
class Solution:
    """
    @param rooms: a list of keys rooms[i]
    @return: can you enter every room
    """
    def canVisitAllRooms(self, rooms):
        # BFS or DFS 
        if rooms is None or len(rooms) == 0:
            return True
        visited = set([0])
        queue = [0]
        while len(queue) > 0:
            room_ind = queue.pop(0)
            for ind in rooms[room_ind]:
                if ind not in visited:
                    visited.add(ind)
                    queue.append(ind)
                    
        return len(visited) == len(rooms)

    
####### DFS top down traverse ########
class Solution:
    """
    @param rooms: a list of keys rooms[i]
    @return: can you enter every room
    """
    def canVisitAllRooms(self, rooms):
        # Write your code here
        visited = set([0])
        self.dfs(0, rooms, visited)
        return len(visited) == len(rooms)
        
    def dfs(self, start, rooms, visited):
        for ind in rooms[start]:
            if ind in visited:
                continue
            visited.add(ind)
            self.dfs(ind, rooms, visited)
            
        return 
    
##### bit wise algo ##
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = 0
        ct = 0
        to_visit = [0]
		
        while to_visit:
            room = to_visit.pop()
			
            mask = 1 << room
            if visited & mask: continue
			
            visited |= mask
            ct += 1
            to_visit.extend(rooms[room])
			
        return ct == len(rooms)
