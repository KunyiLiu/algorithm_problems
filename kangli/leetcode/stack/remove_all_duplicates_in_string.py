class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = [S[0]]
        for i in range(1, len(S)):
            if stack:
                if S[i] == stack[-1]:
                    stack.pop()
                    continue
            stack.append(S[i])
        return "".join(stack)


'''
Success
Details 
Runtime: 84 ms, faster than 61.63% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Memory Usage: 13.9 MB, less than 100.00% of Python3 online submissions for Remove All Adjacent Duplicates In String.
Next challenges: Largest Rectangle in Histogram, Binary Tree Preorder Traversal, Exclusive Time of Functions
'''
