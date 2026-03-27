class Solution:
    def reorganizeString(self, s: str) -> str:
        #  heap - represent the char ready to add to string,
        # max heap based on the count of char in s.
        # prev - block the char for 1 step will add it in the next step
        # Time complexity: O(nlogk), k is the unique chars
        from collections import Counter
        import heapq
        
        prev = None
        char_count = Counter(s)
        maxheap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(maxheap)

        result = []
        while maxheap:
            char = heapq.heappop(maxheap)[1]
            result.append(char)
            char_count[char] -= 1

            if prev:
                heapq.heappush(maxheap, (-char_count[prev], prev))
                # reset prev!
                prev = None

            if char_count[char] > 0:
                prev = char

        if len(result) < len(s):
            return ""

        return ''.join(result)
        

        




        
