class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        # Write your code her
        import heapq
        heap = []
        preps, graph, inds = [], {}, {}
        for i in range(1, len(words)):
            self.add_prep(preps, words[i-1], words[i])
        for word in words:
            for charac in word:
                graph[charac] = []
                inds[charac] = 0
            
        for u, v in preps:
            graph[u].append(v)
            inds[v] += 1 
                
        for ind in inds:
            if inds[ind] == 0:
                # use heapq instead of regular queue so that we can get the 
                # smallest lexicographical order
                heapq.heappush(heap, ind)
        
        result = []  
        # print(graph, inds, preps)
        while len(heap) > 0:
            node = heapq.heappop(heap)
            result.append(node)
            for i in graph.get(node, []):
                inds[i] -= 1 
                if inds[i] == 0:
                    heapq.heappush(heap, i)
                    
        if len(result) == len(inds):
            return ''.join(result)
        else:
            return ''
            
    def add_prep(self, preps, first_word, second_word):
        start = 0
        while start < min(len(first_word), len(second_word)):
            if first_word[start] == second_word[start]:
                start += 1 
            else:
                preps.append((first_word[start], second_word[start]))
                break
        
        return 
