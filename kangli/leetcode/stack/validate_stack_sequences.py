class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0 
        for elt in pushed:
            stack.append(elt)
            while stack and popped[j] == stack[-1]:
                stack.pop()
                j += 1
        if not stack:
            return True
        else:
            return False
            

'''
Success
Details 
Runtime: 92 ms, faster than 22.06% of Python3 online submissions for Validate Stack Sequences.
Memory Usage: 13.6 MB, less than 20.00% of Python3 online submissions for Validate Stack Sequences.
Next challenges: Decoded String at Index, Sum of Subarray Minimums, Check If Word Is Valid After Substitutions
'''
