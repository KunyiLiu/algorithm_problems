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
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # use d&q method 
        # ensure left tree and right tree is Valid
        # then root.left < root < roo.right
        result, _, _ = self.dfs(root)
        return result
        
    def dfs(self, root):
        if root is None:
            return True, None, None
        
        left_valid, leftmin, leftmax = self.dfs(root.left)
        right_valid, rightmin, rightmax = self.dfs(root.right)
        if left_valid and right_valid:
            if leftmax and rightmin:
                is_valid = root.val > leftmax and root.val < rightmin
                rootmin = min(root.val, leftmin, rightmin)
                rootmax = max(root.val, leftmax, rightmax)
            elif leftmax:
                is_valid, rootmin, rootmax = root.val > leftmax, min(root.val, leftmin),\
                max(root.val, leftmax)
            elif rightmin:
                 is_valid, rootmin, rootmax = root.val < rightmin, min(root.val, rightmin),\
                max(root.val, rightmax)
            else:
                is_valid, rootmin, rootmax = True, root.val, root.val
        
            return is_valid, rootmin, rootmax
        return False, None, None
