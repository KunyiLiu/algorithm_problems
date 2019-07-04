class Solution:
    """
    @param: A: An integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def continuousSubarraySum(self, A):
        #  O(n)
        # max_sum, compare with prefix_sum[i] - min(prefix_sum[:i])
        # prefix_sum[i] = sum(A[0] ... A[i-1])
        min_ind, max_sum = 0, - float('inf')
        prefix_sum = [0]
        result = [-1, -1]
        for i, num in enumerate(A):
            cur_sum = prefix_sum[i] + num
            prefix_sum.append(cur_sum)
            if max_sum < cur_sum - prefix_sum[min_ind]:
                max_sum = cur_sum - prefix_sum[min_ind]
                result = [min_ind, i]
            min_ind = i + 1 if cur_sum < prefix_sum[min_ind] else min_ind 
        
        return result
        
        
 ######### enumeration ########
# 枚举即可, 枚举的过程中维护以当前元素结尾的最大和.
# 每次循环把当前元素加到这个和中, 在加上之前判断:
# 如果这个和是负数, 则放弃之前的元素, 把和置为0, 区间左端点设为当前元素
# 如果是正数, 则直接累加.
class Solution:
    # @param {int[]} A an integer array
    # @return {int[]}  A list of integers includes the index of the 
    #                  first number and the index of the last number
    def continuousSubarraySum(self, A):
        ans = -0x7fffffff
        sum = 0
        start, end = 0, -1
        result = [-1, -1]
        for x in A:
            if sum < 0:
                sum = x
                start = end + 1
                end = start
            else:
                sum += x
                end += 1
            if sum > ans:
                ans = sum
                result = [start, end]

        return result
