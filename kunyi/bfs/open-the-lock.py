class Password(object):
    def __init__(self, x, y, k, z):
        self.x = x 
        self.y = y    
        self.k = k  
        self.z = z

class Solution:
    """
    @param deadends: the list of deadends
    @param target: the value of the wheels that will unlock the lock
    @return: the minimum total number of turns 
    """
    
    def openLock(self, deadends, target):
        # Write your code here
        # 2D grid -> 4 grid = 0
        # use hash to record visited passwords
        # queue to record the possible passwords of each attemp - 層級bfs
        from queue import Queue
        if '0000' in deadends:
            return -1 
        deadends = set(deadends)
        queue = Queue()
        queue.put(Password(0, 0, 0, 0))
        visited_hash = {'0000'}
        turn = 0
        while not queue.empty():
            # nth try  
            qsize = queue.qsize()
            for i in range(qsize):
                cur_target = queue.get()
                cur_target_str = ''.join([str(cur_target.x), str(cur_target.y), str(cur_target.k), str(cur_target.z)])
                if cur_target_str == target:
                    return turn
                self.bfs(deadends, cur_target, queue, visited_hash)
            turn += 1 

            
        return -1
                    
                    
    def bfs(self, deadends, target, queue, visited_hash):
        deltaX = [1, -1, 0, 0, 0, 0, 0, 0]
        deltaY = [0, 0, 1, -1, 0, 0, 0, 0]
        deltaK = [0, 0, 0, 0, 1, -1, 0, 0]
        deltaZ = [0, 0, 0, 0, 0, 0, 1, -1]
        
        x, y, k, z = target.x, target.y, target.k, target.z
        for i in range(8):
            new_x = (x + deltaX[i]) % 10   # -1 % 10 = 9
            new_y = (y + deltaY[i]) % 10 
            new_k = (k + deltaK[i]) % 10 
            new_z = (z + deltaZ[i]) % 10 
            new_str = ''.join([str(new_x), str(new_y), str(new_k), str(new_z)])
            if new_str in visited_hash or new_str in deadends:
                continue
            new_target = Password(new_x, new_y, new_k, new_z)
            visited_hash.add(new_str)
            queue.put(new_target)
