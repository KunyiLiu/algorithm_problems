class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-1*i for i in stones]
        while len(stones)>1:
            heapq.heapify(stones)
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)
            diff = s1 - s2 
            if diff != 0:
                heapq.heappush(stones, diff)
        return -1*stones[0] if len(stones) == 1 else 0
        

'''
Success
Details 
Runtime: 36 ms, faster than 82.54% of Python3 online submissions for Last Stone Weight.
Memory Usage: 13.5 MB, less than 100.00% of Python3 online submissions for Last Stone Weight.
Next challenges: Sliding Window Maximum, Bag of Tokens, Minimum Domino Rotations For Equal Row

Related Topics: Heap, Greedy
Hint: Simulate the process. We can do it with a heap, or by sorting some list of stones every time we take a turn. 
'''
