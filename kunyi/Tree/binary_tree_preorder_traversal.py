"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        # using current pointer 
        current = root 
        result, stack = [], []
        while len(stack) > 0 or current is not None:
            if current is not None:
                result.append(current.val)
                stack.append(current)
                current = current.left 
                
            else:
                current = stack.pop()
                current = current.right 
                
        return result
