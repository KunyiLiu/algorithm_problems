"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root
    @return: the same tree where every subtree (of the given tree) not containing a 1 has been removed
    """
    def pruneTree(self, root):
        # Write your code here
        if root is None:
            return 
        is_included = self.dfs(root)
        return root if is_included else None
        
    def dfs(self, root):
        # if it includes 1, None counted as no 
        if root is None:
            return False 
            
        is_left_included = self.dfs(root.left)
        is_right_included = self.dfs(root.right)
        is_included = is_left_included or is_right_included or root.val == 1 
        if not is_left_included:
            root.left = None 
        if not is_right_included:
            root.right = None 
            
        return is_included
        
 ############### Method 2 ############
 class Solution:
    """
    @param root: the root
    @return: the same tree where every subtree (of the given tree) not containing a 1 has been removed
    """
    def pruneTree(self, root):
        if root is None:
            return None
        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)
        if root.val == 0 and root.left == None and root.right == None:
            return None 
        else:
            return root
