class HitCounter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # {timestamp: hit_count} or
        # [0]*300 requires more time when over 300
        # time, space - constant time 300
        # queue - first in first out
        self.queue = []
        self.count = 0
        

    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        #  self.last_visited - 299 -> self.last_visited
        self.queue.append(timestamp)
        self.count += 1
        

    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while len(self.queue) > 0 and timestamp - self.queue[0] >= 300:
            self.queue.pop(0)
            self.count -= 1 
        
        return self.count


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
