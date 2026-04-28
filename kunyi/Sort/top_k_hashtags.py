from collections import defaultdict

### bucket sort #####
class Solution:
    def pickKHash(self, events, k):
        # time complexity: O(N + MlogM), where N = #events; M = #unique hashtags 
        hash_to_uids = defaultdict(set)

        for uid, hashtag in events:
            # assume all lowercase
            hash_to_uids[hashtag].add(uid)

        # create a count to list of hashtags (sorted)
        freq_to_hash = defaultdict(list)
        for hash, uids in hash_to_uids.items():
            cnt = len(uids)
            freq_to_hash[cnt].append(hash)

        n = len(events)
        # start from n freq
        result = []
        for i in range(n, -1, -1):
            if i not in freq_to_hash:
                continue
            
            result.extend(sorted(freq_to_hash[i]))
            if len(result) >= k:
                break
        
        return result[:(k+1)]


####### minheap, use ReverseObj #####
import heapq
from collections import defaultdict

class Solution:
    def getTopKHashtags(self, events, k):
        # 1. Count unique users per hashtag
        hash_to_users = defaultdict(set)
        for uid, hashtag in events:
            hash_to_users[hashtag].add(uid)
        
        # 2. Use a Min-Heap to keep only the top K
        min_heap = []
        
        for hashtag, users in hash_to_users.items():
            count = len(users)
            
            # We wrap the count and hashtag. 
            # Note: To handle the alphabetical tie-break in a MIN-heap, 
            # we need the 'worst' alphabetical (the larger string) 
            # to be at the top of the heap.
            # Python's heapq compares tuples element by element.
            heapq.heappush(min_heap, (count, ReverseStr(hashtag)))
            
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # 3. Extract and sort the remaining K elements
        # Since it's a min-heap, we pop them out and reverse
        result = []
        while min_heap:
            count, rev_tag = heapq.heappop(min_heap)
            result.append(rev_tag.val)
            
        return result[::-1]

# Helper class to flip string comparisons for the Min-Heap
class ReverseStr:
    def __init__(self, val):
        self.val = val
    def __lt__(self, other):
        # This makes "z" < "a", so "z" stays at the top of the Min-Heap
        return self.val > other.val
