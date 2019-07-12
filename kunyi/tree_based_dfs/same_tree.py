############# traversal ##################
class Solution:
    """
    @param a: the root of binary tree a.
    @param b: the root of binary tree b.
    @return: true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # inorder check 
        self.is_same = True 
        self.helper(a, b)
        return self.is_same
        
    def helper(self, a, b):
        # normal exits
        if a is None and b is None:
            return
        # two wrong exits: 1. structure, 2.error
        if a is None or b is None:
            self.is_same = False
            return 
        if a.val != b.val:
            self.is_same = False 
            return 
        self.helper(a.left, b.left)
        self.helper(a.right, b.right)
            
        return 

############## DQ ########################
class Solution:
    """
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        # Write your code here
        if a == None and b == None: return True
        if a and b and a.val == b.val:
            return self.isIdentical(a.left, b.left) and \
                    self.isIdentical(a.right, b.right)
        return False
