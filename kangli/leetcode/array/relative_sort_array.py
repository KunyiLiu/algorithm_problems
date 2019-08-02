class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        from collections import Counter
        counts = Counter(arr1)
        res, remain = [], []
        for n in arr2:
            res.extend([n]*counts[n])
            del counts[n]
        for k, v in counts.items():
            remain.extend([k]*v)
        return res + sorted(remain)
        

'''
Success
Details 
Runtime: 40 ms, faster than 91.50% of Python3 online submissions for Relative Sort Array.
Memory Usage: 13.8 MB, less than 100.00% of Python3 online submissions for Relative Sort Array.
Next challenges: Insertion Sort List, Maximum Distance in Arrays, Sum of Digits in the Minimum Number
'''
