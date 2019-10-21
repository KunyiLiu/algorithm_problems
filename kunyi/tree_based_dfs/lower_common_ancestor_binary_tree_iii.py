"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: The root of the tree
    @param: A: node in the tree
    @param: B: node in the tree
    @return: The lowest common ancestor of A and B
    """
    def lowestCommonAncestorII(self, root, A, B):
        # use dict to record its path from A to root 
        # first common parent
        hash_set = set()
        while A is not None:
            hash_set.add(A)
            A = A.parent 
            
            
        while B is not None:
            if B in hash_set:
                return B 
                
            B = B.parent 
            
        return
