class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Try merge sort, Time is also O(nlogn), but space is O(n)
        n = len(nums)
        if n <= 1:
            return nums

        return self.merge_sort(nums, 0, n - 1)

    def merge_sort(self, nums, start, end):
        if start == end:
            return [nums[start]]
        
        mid = start + (end - start) // 2
        left_arr = self.merge_sort(nums, start, mid)
        right_arr = self.merge_sort(nums, mid + 1, end)
        return self.merge_arrays(left_arr, right_arr)

    def merge_arrays(self, left_arr, right_arr):
        res = []
        l, r = 0, 0 
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] < right_arr[r]:
                res.append(left_arr[l])
                l += 1
            else:
                res.append(right_arr[r])
                r += 1 

        while l < len(left_arr):
            res.append(left_arr[l])
            l += 1

        while r < len(right_arr):
            res.append(right_arr[r])
            r += 1

        return res
