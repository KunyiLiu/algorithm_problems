"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

class ResultType:
    def __init__(self, root=None, is_A=False, is_B=False):
        self.root = root 
        self.is_A = is_A
        self.is_B = is_B

class Solution:
    """
    @param: root: The root of the binary tree.
    @param: A: A TreeNode
    @param: B: A TreeNode
    @return: Return the LCA of the two nodes.
    """
    def lowestCommonAncestor3(self, root, A, B):
        # write your code here
        result = self.helper(root, A, B)
        return result.root if result.is_A and result.is_B else None 
        
    def helper(self, root, A, B):
        if root is None:
            return ResultType()
            
        left = self.helper(root.left, A, B)
        right = self.helper(root.right, A, B)
        if left.is_A and left.is_B:
            return left 
            
        if right.is_A and right.is_B:
            return right 
            
        result = ResultType(root, left.is_A or right.is_A or root == A, left.is_B or right.is_B or root == B )
        
        return result
