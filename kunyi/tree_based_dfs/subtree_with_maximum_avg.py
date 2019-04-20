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
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        import sys
        self.max_avg = -sys.maxsize - 1
        self.result = None 
        self.helper(root)
        return self.result 
        
    def helper(self, root):
        if root is None: 
            return 0, 0 
            
        left_sum, left_node = self.helper(root.left)
        right_sum, right_node = self.helper(root.right)
        cur_sum = left_sum + right_sum + root.val 
        cur_node = left_node + right_node + 1 
        if cur_sum / float(cur_node) > self.max_avg:
            self.max_avg = cur_sum / float(cur_node)
            self.result = root 
            
        return cur_sum, cur_node
