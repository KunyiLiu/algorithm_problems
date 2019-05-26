class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        # for loop, each loop do a 2sum O(n^2)
        # hash_table to record the first value: list of tuples = -first_value
        # the problem falls into how to avoid duplication: 1. hash + set 
        # 2. if i and nums[i] == nums[i - 1]:
        hash_table = {}
        numbers = sorted(numbers)
        for i in range(len(numbers)):
            if numbers[i] not in hash_table:
                hash_table[numbers[i]] = set([])
                self.two_sum(numbers[i+1:], -numbers[i], hash_table[numbers[i]])
        
        results = []
        for key, value_list in hash_table.iteritems():
            tmp = [[key, tup[0], tup[1]] for tup in value_list]
            results.extend(tmp)
            
        return results
        
    def two_sum(self, array, target, record_list):
        start, end = 0, len(array) - 1 
        while start < end:
            if array[start] + array[end] < target:
                start += 1 
            elif array[start] + array[end] > target:
                end -= 1 
            else:
                record_list.add((array[start], array[end]))
                start += 1 
                end -= 1 
                
####### another way to deal with duplication ##############
class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, nums):
        nums.sort()
        results = []
        length = len(nums)
        for i in range(0, length - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            self.find_two_sum(nums, i + 1, length - 1, -nums[i], results)
        return results

    def find_two_sum(self, nums, left, right, target, results):
        while left < right:
            if nums[left] + nums[right] == target:
                results.append([-target, nums[left], nums[right]])
                right -= 1
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
