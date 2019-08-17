class Solution:
    def maxSatisfied(self, customers, grumpy, X):
        initial_happy = 0 
        for i in range(len(customers)):
            if not grumpy[i]:
                initial_happy += customers[i]
                customers[i] = 0 
        max_sub_sum = sum(customers[0:X])
        cur_sum = max_sub_sum
        left, right = 0, X-1 
        if X == 1:
            return max(customers) + initial_happy
        while right < len(customers)-1: 
            right += 1
            cur_sum = cur_sum - customers[left] + customers[right]
            left += 1
            max_sub_sum = max(max_sub_sum, cur_sum)
        return max_sub_sum + initial_happy


'''
Success
Details 
Runtime: 332 ms, faster than 70.17% of Python3 online submissions for Grumpy Bookstore Owner.
Memory Usage: 15.8 MB, less than 100.00% of Python3 online submissions for Grumpy Bookstore Owner.
Next challenges: Combination Sum, Remove Duplicates from Sorted Array II, Pascal's Triangle II

Related Topics: Array, Sliding Window
Hint: Say the store owner uses their power in minute 1 to X and we have some answer A. If they instead use their power
from minute 2 to X+1,we only have to use data from minutes 1, 2, X and X+1 to update our answer A.
'''
