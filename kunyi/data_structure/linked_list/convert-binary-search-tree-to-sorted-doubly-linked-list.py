"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of a tree
    @return: head node of a doubly linked list
    """
    def treeToDoublyList(self, root):
        # inorder traverse - sorted 
        if root is None:
            return 
        
        left_head, right_tail = self.helper(root)
        left_head.left = right_tail
        right_tail.right = left_head
        
        return left_head
        
    def helper(self, root):
        # not use root.left and root.right 
        if root is None:
            return root, root 
            
        left_small, left_large = self.helper(root.left)
        right_small, right_large = self.helper(root.right)
        if left_large is None:
            root.left = left_large
            root.right = right_small
            if right_small:
                right_small.left = root 
            else:
                right_large = root 
            return root, right_large
        else:
            left_large.right = root 
            root.left = left_large
            root.right = right_small
            if right_small:
                right_small.left = root 
            else:
                right_large = root 
                
            return left_small, right_large
