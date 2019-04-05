"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the minimum subtree
    """
    def findSubtree(self, root):
        # write your code here
        import sys
        self.result, self.min_sum = None, sys.maxsize
        self.helper(root)
        return self.result 
        
        
    def helper(self, root):
        # return sum of subtree with root as root
        if root is None:
            return 0 
            
        left_sum = self.helper(root.left)
        right_sum = self.helper(root.right)
        cur_sum = left_sum + right_sum + root.val 
        if cur_sum < self.min_sum:
            self.min_sum = cur_sum
            self.result = root 
            
        return cur_sum
