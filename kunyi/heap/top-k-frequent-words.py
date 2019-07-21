class Solution:
    """
    @param words: an array of string
    @param k: An integer
    @return: an array of string
    """
    def topKFrequentWords(self, words, k):
        # heapify (-count, word)
        from collections import Counter 
        import heapq 
        count_dict = Counter(words)
        heap = [(-v, k) for k, v in count_dict.items()]
        heapq.heapify(heap)
        # error [heap[i][1] for i in range(k)]
        return [heapq.heappop(heap)[1] for i in range(k)]
