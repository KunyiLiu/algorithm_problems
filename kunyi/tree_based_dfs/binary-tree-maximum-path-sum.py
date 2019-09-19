"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """
    def maxPathSum(self, root):
        # find the lonest and second longest path sum 
        if root is None:
            return 0 
            
        max_path, _ = self.helper(root)
        return max_path
        
    def helper(self, root):
        # max_path - can be any node to any node, at least one node 
        # single_path - from root to any, can with no node 
        import sys 
        if root is None:
            return -sys.maxsize, 0 
            
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        single_path = max(0, left[1] + root.val, right[1] + root.val)
        max_path = max(left[0], right[0], left[1] + right[1] + root.val)
        
        return max_path, single_path
