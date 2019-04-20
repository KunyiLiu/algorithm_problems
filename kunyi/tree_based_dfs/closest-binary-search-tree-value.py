"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        # recursion DQ O(h), BST 并不保证树高是 logn 
        import sys
        self.result = None
        self.diff = sys.maxsize
        self.helper(root, target)
        return self.result.val 
        
    def helper(self, root, target):
        if root is None:
            return 
        
        diff = abs(root.val - target)
        if diff < self.diff:
            self.result = root 
            self.diff = diff 
            
        if root.val > target:
            self.helper(root.left, target)
        else:
            self.helper(root.right, target)
            
        return
    
    # method2: upper and lower bound 
    class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @return: the value in the BST that is closest to the target
    """
    def closestValue(self, root, target):
        upper = root
        lower = root
        while root:
            if target > root.val:
                lower = root
                root = root.right
            elif target < root.val:
                upper = root
                root = root.left
            else:
                return root.val
        if abs(upper.val - target) <= abs(lower.val - target):
            return upper.val
        return lower.val
