"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a TreeNode, the root of the binary tree
    @return: nothing
    """
    def invertBinaryTree(self, root):
        # write your code here
        self.helper(root)
        return root 
        
    def helper(self, root):
        if root is None:
            return root 
            
        left_subtree = self.helper(root.left)
        right_subtree = self.helper(root.right)
        root.left = right_subtree
        root.right = left_subtree
        return root 
