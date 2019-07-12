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
    def maxDepth(self, root):
        # write your code here
        if root == {}:
            return 0
        result = self.dfs(root)
        return result
        
    def dfs(self, root):
        if root is None:
            return 0
            
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        height = max(left, right) + 1 
        return height
