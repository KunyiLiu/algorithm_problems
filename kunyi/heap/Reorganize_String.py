class Solution:
    def reorganizeString(self, s: str) -> str:
        #  heap - represent the char ready to add to string,
        # max heap based on the count of char in s.
        # prev - block the char for 1 step will add it in the next step
        from collections import Counter
        import heapq
        
        prev = None
        char_count = Counter(s)
        maxheap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(maxheap)

        result = []
        while maxheap:
            cnt, char = heapq.heappop(maxheap)

            if result and result[-1] == char:
                if not maxheap:
                    return ""  # impossible
                cnt1, char1 = heapq.heappop(maxheap)
                result.append(char1)
                cnt1 += 1

                if cnt1 < 0:
                    heapq.heappush(maxheap, (cnt1, char1))

                heapq.heappush(maxheap, (cnt, char))

            else:
                result.append(char)
                cnt += 1

                if cnt < 0:
                    heapq.heappush(maxheap, (cnt, char))

        return ''.join(result)
                

            
        

        




        
