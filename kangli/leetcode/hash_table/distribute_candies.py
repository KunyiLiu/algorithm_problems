import math
class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        counts = {}
        for c in candies:
            if c not in counts:
                counts[c] = 1
            else:
                counts[c] += 1
        brother_count, sis_count = 0, 0
        for c, v in counts.items():
            brother_count += v-1
            sis_count += 1
        if sis_count <= brother_count:
            return sis_count
        else:
            return math.floor(sis_count - (sis_count-brother_count)/2)
'''
Success
Details 
Runtime: 196 ms, faster than 14.04% of Python3 online submissions for Distribute Candies.
Memory Usage: 14.7 MB, less than 55.43% of Python3 online submissions for Distribute Candies.
Next challenges:
Isomorphic Strings, Binary Subarrays With Sum, Time Based Key-Value Store
Related Topics: Hash Table 
To maximize the number of kinds of candies, we should try to distribute candies such that sister will gain all kinds.
What is the upper limit of the number of kinds of candies sister will gain? Remember candies are to distributed equally.
Which data structure is the most suitable for finding the number of kinds of candies?
Will hashset solves the problem? Inserting all candies kind in the hashset and then checking its size with upper limit.
'''
