class Solution(object):
    def twoSum(self, numbers, target):
        i1, i2 = 0, len(numbers) - 1
        while i1 <= i2:
            s = numbers[i1] + numbers[i2]
            if s == target:
                return [i1 + 1, i2 + 1]
            elif s < target:
                i1 += 1
            elif s > target:
                i2 -= 1

'''

17 / 17 test cases passed.
Status: Accepted
Runtime: 44 ms
Memory Usage: 11.9 MB

Similar Questions:
Two Sum, Two Sum IV - Input is a BST
'''
