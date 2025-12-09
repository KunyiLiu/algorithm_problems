class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Try count sort, Time: O(n + k), K is the range between min and max values
        # spce: O(n)
        from collections import Counter
        counter = Counter(nums)
        res = []
        min_val, max_val = min(nums), max(nums)

        for num in range(min_val, max_val + 1):
            if counter[num] > 0:
                res.extend([num] * counter[num])

        return res
