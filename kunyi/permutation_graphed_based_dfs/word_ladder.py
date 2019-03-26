
class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # build index {'ht': ['hit', 'hot' ..], 'dt'
        # create a generator to yield valid new words for start_word
        # use bfs (level-order) to record distance when hit end
        if dict is None or len(dict) == 0:
            return 0 
        
        self.dict = dict
        self.dict.add(start)
        self.dict.add(end)
        length = len(start)
        self.indexes = self.build_index(length)
        result = self.bfs(start, end)
        return result 
        
    def build_index(self, length):
        indexes = []
        for i in range(length):
            index = {}
            for word in self.dict:
                prefix = word[:i] + word[(i+1):]
                if prefix not in index:
                    index[prefix] = []
                index[prefix].append(word)
            indexes.append(index)
                
        return indexes
        
    def get_next_word(self, start_word):
        for i in range(len(start_word)):
            tmp = start_word[:i] + start_word[(i+1):]
            if tmp in self.indexes[i]:
                for j in self.indexes[i][tmp]:
                    if j != start_word:
                        yield j 
                        
    def bfs(self, start, end):
        import queue
        queue = queue.Queue()
        visited = set()
        queue.put(start)
        distance = 1 
        while not queue.empty():
            qsize = queue.qsize()
            for i in range(qsize):
                word = queue.get()
                visited.add(word)
                if word == end:
                    return distance
                for new_word in self.get_next_word(word):
                    if new_word not in visited:
                        queue.put(new_word)
            distance += 1 
        
        return 0

# correct
 class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, dict):
        # write your code here
        if dict is None or len(dict) == 0:
            return -1
        import Queue
        q = Queue.Queue()
        q.put(start)
        length = 1
        dict.add(end)
        while not q.empty():
            size = q.qsize()
            for ind in range(size):
                word = q.get()
                if word == end:
                    return length
                #print("word:",word)
                for i in range(len(word)):
                    for letter in range(97, 123):
                        if chr(letter) != word[i]:
                            tmp = word[:i] + chr(letter) + word[(i+1):]
                            if tmp in dict:
                                q.put(tmp)
                                dict.remove(tmp)
            length += 1
            
        return -1
