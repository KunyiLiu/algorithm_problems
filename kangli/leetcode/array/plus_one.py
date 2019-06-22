class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits)-1
        digits[-1] += 1
        while i > 0:
            if digits[i] != 10:
                break
            digits[i] = 0
            digits[i-1] +=1
            i -= 1
        if digits[0] == 10:
            digits[0]=0
            digits.insert(0, 1)
        return digits
'''
Success
Details 
Runtime: 36 ms, faster than 97.98% of Python3 online submissions for Plus One.
Memory Usage: 13.2 MB, less than 5.29% of Python3 online submissions for Plus One.
Next challenges:
Multiply Strings
Add Binary
Plus One Linked List

Related Topics: Array
Similar Questions: Multiply Strings, Add Binary, Plus One Linked List,
Add to Array-Form of Integer
Easy
'''
