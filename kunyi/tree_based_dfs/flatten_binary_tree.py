"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: a TreeNode, the root of the binary tree
    @return: 
    """
    def flatten(self, root):
        # write your code here
        node = None
        if root is None:
            return node
        self.flatten(root.left)
        self.flatten(root.right)

        tmp = root.right
        root.right = root.left
        root.left = None
        node = root
        while node.right:
            node = node.right
        node.right = tmp
  
            
        
        return root
