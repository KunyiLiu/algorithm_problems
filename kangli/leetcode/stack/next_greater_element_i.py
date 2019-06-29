class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack, d = [], {}
        res = []
        for n in nums2:
            while stack and n > stack[-1]:
                d[stack.pop()] = n
            stack.append(n)
        for n in nums1:
            if n in d:
                res.append(d[n])
            else:
                res.append(-1)
        return res

'''
Success
Details
Runtime: 40 ms, faster than 95.02% of Python3 online submissions for Next Greater Element I.
Memory Usage: 13.4 MB, less than 15.93% of Python3 online submissions for Next Greater Element I.
Next challenges:
Next Greater Element II
Next Greater Element III

Related Topics: Stack
Similar Questions: Next Greater Element II
Medium
Next Greater Element III
Medium
Daily Temperatures
Medium 
'''
