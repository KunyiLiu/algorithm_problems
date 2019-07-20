"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ResultType:
    def __init__(self, root = None, isA = False, isB = False):
        self.root = root
        self.isA = isA
        self.isB = isB

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        result = self.helper(root, A, B)
        return result.root
    
    def helper(self, root, A, B):
        # resultType = return root, is_left_lca, is_right_lca
        result = ResultType()
        if root is None:
            return result
        left = self.helper( root.left, A, B)
        right = self.helper(root.right, A, B)
        if left.isA and left.isB:
            return left
        if right.isA and right.isB:
            return right
        result.isA = left.isA or right.isA
        result.isB = left.isB or right.isB
        result.root = root
        if root == A:
            result.isA = True
        if root == B:
            result.isB = True
        return result
    
    
# Method 2
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
class ResultType:
    def __init__(self, root = None, isA = False, isB = False):
        self.root = root
        self.isA = isA
        self.isB = isB

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # write your code here
        result = self.helper(root, A, B)
        return result.root
    
    def helper(self, root, A, B):
        result = ResultType()
        if root is None:
            return result
        left = self.helper( root.left, A, B)
        right = self.helper(root.right, A, B)
        if left.isA and left.isB:
            return left
        if right.isA and right.isB:
            return right
        result.isA = left.isA or right.isA
        result.isB = left.isB or right.isB
        result.root = root
        if root == A:
            result.isA = True
        if root == B:
            result.isB = True
        return result
    
####### customized ########
class ResultType:
    def __init__(self):
        self.is_a = False
        self.is_b = False
        self.lca = None

class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: A: A TreeNode in a Binary.
    @param: B: A TreeNode in a Binary.
    @return: Return the least common ancestor(LCA) of the two nodes.
    """
    def lowestCommonAncestor(self, root, A, B):
        # botton up, DQ 
        result = self.dfs(root, A, B)
        return result.lca
        
    def dfs(self, root, A, B):
        if root is None:
            return ResultType()
            
        left_result = self.dfs(root.left, A, B)
        right_result = self.dfs(root.right, A, B)
        # iteration - break;
        # recursion: dq - keep the same resultType; traverse - only change when requirements met 
        if left_result.is_a and left_result.is_b:
            return left_result
        if right_result.is_a and right_result.is_b:
            return right_result
        result = ResultType()
        result.is_a = left_result.is_a or right_result.is_a or root == A 
        result.is_b = left_result.is_b or right_result.is_b or root == B 
        if result.is_a and result.is_b:
            result.lca = root
        return result 

