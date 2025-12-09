class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # use partition sort 
        n = len(nums)
        if n <= 1:
            return nums

        self.heapify(nums)
        # after create the max heap, move max to the end, and then restore the remaining heap
        for end in range(n - 1, -1, -1):
            nums[0], nums[end] = nums[end], nums[0]
            self.shift_down(nums, 0, end) # restore heap in [0,end)
        return nums

    def heapify(self, nums):
        n = len(nums)
        for parent in range((n - 1)// 2, -1, -1):
            # from the sub-parent to the parent
            self.shift_down(nums, parent, n)

    def shift_down(self, nums, parent, end):
        # end is exclusive
        while True:
            left = parent * 2 + 1
            right = parent * 2 + 2
            largest = parent
            if left < end and nums[left] > nums[largest]:
                largest = left
            if right < end and nums[right] > nums[largest]:
                largest = right

            if largest == parent:
                break
            nums[parent], nums[largest] = nums[largest], nums[parent]
            # continue the loop
            parent = largest

