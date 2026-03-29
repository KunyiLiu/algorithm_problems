import heapq

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxheap = []
        
        for count, char in [(a, 'a'), (b, 'b'), (c, 'c')]:
            if count > 0:
                heapq.heappush(maxheap, (-count, char))
        
        result = []

        while maxheap:
            count1, char1 = heapq.heappop(maxheap)

            # Check if adding char1 causes 3 consecutive chars
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not maxheap:
                    break  # no alternative → stop

                # try next char
                count2, char2 = heapq.heappop(maxheap)
                result.append(char2)
                count2 += 1  # since negative

                if count2 < 0:
                    heapq.heappush(maxheap, (count2, char2))

                heapq.heappush(maxheap, (count1, char1))
            else:
                result.append(char1)
                count1 += 1

                if count1 < 0:
                    heapq.heappush(maxheap, (count1, char1))

        return ''.join(result)
