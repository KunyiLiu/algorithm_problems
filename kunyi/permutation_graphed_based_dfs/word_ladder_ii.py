class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    # get entry: word[:i] + word[(i+1):]
    # build indexes from dict: [{'ot':['hot','dot','dog'..],..},{'ht'..},{'ho':}]
    ## only used in getNextword
    # next word: change one letter from 1 to len(word) 
    # bfs build distance:  from start to end ( do not use word in dict twice)
    # dfs: exit when cur == target; use getNextword, distance condition
    def findLadders(self, start, end, dict):
        # write your code here
        if len(dict) == 0 or len(start) != len(end):
            return []
        self.result = []
        dict.update([end])
        self.dict = dict
        self.distance = {} # end, start
        self.Indexes = self.buildIndexes(len(start))
        self.buildDistance(start, end) 
        if end in self.distance:
          self.dfs(start, end, [start])
        return self.result
    
    def buildIndexes(self, length):
        Indexes = []
        for i in range(length):
            Index = {}
            for word in self.dict:
                entry = word[:i] + word[(i+1):]
                value = Index.get(entry, [])
                value.append(word)
                Index[entry] = value
            Indexes.append(Index)
        return Indexes
        
    def getNextword(self, word):
        # yield next word or return list
        for i in range(len(word)):
            entry = word[:i] + word[(i+1):]
            if entry in self.Indexes[i]:
                for next in self.Indexes[i][entry]:
                    if next != word:
                        yield next
    
    def buildDistance(self, start, end):
        # for shortest path , record distance
        self.distance = {start:0}
        import queue
        q = queue.Queue()
        q.put(start)
        while not q.empty():
            word = q.get()
            for next in self.getNextword(word):
                if next not in self.distance:
                    q.put(next)
                    self.distance[next] = self.distance[word] + 1
        
    def dfs(self, cur, end, path):
        if cur == end:
            self.result.append(path)
            return
        for word in self.getNextword(cur):
            if word in self.distance:
                if self.distance[word] - 1 == self.distance[cur]:
                    self.dfs(word, end, path + [word])
