######## TLE O(n^2)  ###############
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the number of subarrays where the product of all the elements in the subarray is less than k
    """
    def numSubarrayProductLessThanK(self, nums, k):
        # O(n^2)
        ans = 0 
        cur_product = 1 
        sub_product = {1: 1}
        for i, num in enumerate(nums):
            cur_product *= num 
            sub_product[i] = cur_product
            if cur_product >= k:
                for j in range(i):
                    if sub_product[i] < k * sub_product[j]:
                        break 
                else:
                    continue
                ans += (i-j)
            else:
                ans += (i+1)
                
        return ans 
        
########### O(n) ########
# 维护一个滑动窗口，left为窗口的左端点，i用来探索下一个数，left和i组成的滑动窗口为[left, i]
# 如果当前窗口中的所有数的乘积 >= k， 说明窗口不再满足条件( < k), 则把left指向的左端点的数从窗口中去掉，反映在窗口乘积上应该是除以要删除的这个数，然后left++，一直重复下去直到窗口再次满足条件，则又找到了一个新的窗口，窗口的长度就是当前窗口中满足条件的子数组个数，
# 窗口长度用 i - left + 1来表示。
class Solution:
    """
    @param nums: an array
    @param k: an integer
    @return: the number of subarrays where the product of all the elements in the subarray is less than k
    """
    def numSubarrayProductLessThanK(self, nums, k):
        # special case [1, 2, 3], 0
        # start will be 1 greater than i
        ans = 0 
        cur_product, start = 1, 0
        for i, num in enumerate(nums):
            cur_product *= num 
            while cur_product >= k and start <= i:
                cur_product //= nums[start]
                start += 1 

            ans += (i - start + 1)
                
        return ans 
