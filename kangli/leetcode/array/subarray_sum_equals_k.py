
#TLE solution with prefix sums
class Solution:
    def subarraySum(self, nums, k):
        prefix_sums = [0 for _ in range(len(nums))]
        prefix_sums[0] = nums[0]
        count = 0
        for i in range(1, len(nums)):
            prefix_sums[i] = prefix_sums[i-1] + nums[i]
        for i in range(len(nums)):
            if prefix_sums[i] == k:
                count += 1
            for j in range(i+1, len(nums)):
                if prefix_sums[j] - prefix_sums[i] == k:
                    count += 1
        return count

'''
Note: Uses prefix sums
Related Topcs: Array, Hash Table
Similar Questions: Two Sum, Continuous Subarray Sum, Subarray Product Less Than K, 
Find Pivot Index, Subarray Sums Divisible by K

Hints: 1) Will Brute force work here? Try to optimize it.
2) Can we optimize it by using some extra space?
3) What about storing sum frequencies in a hash table? Will it be useful?
4) sum(i,j)=sum(0,j)-sum(0,i), where sum(i,j) represents the sum of all the elements from index i to j-1. Can we use this property to optimize it.
'''
