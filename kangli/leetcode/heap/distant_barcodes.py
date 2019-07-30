# sample 484 ms submission
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        from collections import Counter
        data = Counter(barcodes)
        modes = data.most_common()
        l = len(barcodes)
        res = [0] * l
        num, count = modes.pop(0)
        for i in range(0, l, 2):
            res[i] = num
            count -= 1
            if count == 0 and modes:
                num, count = modes.pop(0)
        
        for j in range(1, l, 2):
            res[j] = num
            count -= 1
            if count == 0 and modes:
                num, count = modes.pop(0)
        
        return res
 

'''
Success
Details 
Runtime: 588 ms, faster than 29.55% of Python3 online submissions for Distant Barcodes.
Memory Usage: 15.9 MB, less than 100.00% of Python3 online submissions for Distant Barcodes.
Next challenges: Meeting Rooms II, Best Meeting Point, Find K Pairs with Smallest Sums
'''
