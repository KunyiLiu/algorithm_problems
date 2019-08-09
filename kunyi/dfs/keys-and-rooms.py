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
