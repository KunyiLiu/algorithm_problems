"""
Input: 
timestamps = [1, 5, 2, 7, 10, 12, 6], windowSize = 4

Output: 
3

Explanation
First, sort the timestamps: [1, 2, 5, 6, 7, 10, 12].
Consider windows of size 4:
- Window [1, 5) includes [1, 2]. Count = 2.
- Window [2, 6) includes [2, 5]. Count = 2.
- Window [5, 9) includes [5, 6, 7]. Count = 3.
- Window [6, 10) includes [6, 7]. Count = 2.
- Window [7, 11) includes [7, 10]. Count = 2.
- Window [10, 14) includes [10, 12]. Count = 2.
- Window [12, 16) includes [12]. Count = 1.
The maximum count observed is 3.
"""

class Solution:
    def maxRequests(self, timestamps, windowSize):
        if len(timestamps) == 0 or windowSize == 0:
            return 0

        timestamps.sort()
        # using sliding window, l, r pointer
        l, r = 0, 0
        n = len(timestamps)
        result = 0
        while r < n:
            # move r 
            while r < n and timestamps[r] < timestamps[l] + windowSize:
                r += 1

            # reset the result
            result = max(result, r - l)

            # update l
            l += 1

        return result

sol = Solution()
result = sol.maxRequests([5, 5, 5], 1)
print(f"result is {result}")


###### clean r loop
class Solution:
    def maxRequests(self, timestamps: list[int], window_size: int) -> int:
        if not timestamps or window_size <= 0:
            return 0

        # Sort timestamps to enable a valid sliding window
        timestamps.sort()
        
        max_requests = 0
        l = 0
        n = len(timestamps)
        
        # Expand the window using the right pointer
        for r in range(n):
            # Shrink the window from the left if the current element is out of the window bounds
            while timestamps[r] - timestamps[l] >= window_size:
                l += 1
                
            # The number of valid requests in the current window is (r - l + 1)
            max_requests = max(max_requests, r - l + 1)
            
        return max_requests
