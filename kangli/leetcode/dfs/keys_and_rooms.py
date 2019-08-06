class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        self.dfs(0, rooms, visited)
        return len(visited) == len(rooms)
    
    def dfs(self, cur_room, rooms, visited):
        if cur_room not in visited:
            visited.add(cur_room)
            for key in rooms[cur_room]:
                self.dfs(key, rooms, visited)
             
             
'''
Success
Details 
Runtime: 80 ms, faster than 48.97% of Python3 online submissions for Keys and Rooms.
Memory Usage: 14.5 MB, less than 5.13% of Python3 online submissions for Keys and Rooms.
Next challenges: Convert Sorted Array to Binary Search Tree, Find Eventual Safe States, Robot Room Cleaner
'''


#bfs solution, traverses entire "graph"
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        from collections import deque
        queue = deque([0])
        visited = set()
        while queue:
            cur_room = queue.popleft()
            visited.add(cur_room)
            for key in rooms[cur_room]:
                if key not in visited:
                    queue.append(key)
                    visited.add(key)
        return len(visited) == len(rooms)
        
        
'''
67 / 67 test cases passed.
Status: Accepted
Runtime: 76 ms
Memory Usage: 14.2 MB
'''
