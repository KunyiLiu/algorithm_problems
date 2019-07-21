"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: root of the tree
    @param p: the node p
    @param q: the node q
    @return: find the LCA of p and q
    """
    def lowestCommonAncestor(self, root, p, q):
        # write your code here
        if not all([root, p, q]):
            return None 
        
        smaller_val = min(p.val, q.val)
        larger_val = max(p.val, q.val)
        while True:
            if smaller_val <= root.val and larger_val >= root.val:
                return root 
            if smaller_val > root.val:
                root = root.right 
            if larger_val < root.val:
                root = root.left 
