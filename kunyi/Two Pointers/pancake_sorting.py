class Solution:
    def pancake_sorting(self, nums):
        curr_size = len(nums)
        while curr_size > 1:
            max_ind = self.find_max_index(nums, 0, curr_size - 1)
            if max_ind != curr_size - 1:
                nums[max_ind], nums[curr_size - 1] = nums[curr_size - 1], nums[max_ind]

            curr_size -= 1

        return nums

    def find_max_index(self, nums, left, right):
        max_ind = left
        for i in range(left + 1, right + 1):
            if nums[i] > nums[max_ind]:
                max_ind = i

        return max_ind


if __name__ == '__main__':
    nums = [2,3,5,1,8]
    print('The result is {}'.format(Solution().pancake_sorting(nums)))
