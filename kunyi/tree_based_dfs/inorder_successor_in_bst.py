"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Solution:
    def inorderSuccessor(self, root, p):
        if not root:
            return None
        
        # If root is less than or equal to p, the successor MUST be in the right
        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)
        
        # If root is greater than p, the successor is either in the left
        # OR it is the root itself (if left returns None)
        left = self.inorderSuccessor(root.left, p)
        return left if left else root


class Solution:
    def inorderSuccessor(self, root, p):
        successor = None
        while root:
            if root.val > p.val:
                # Potential candidate! Save it and look for something smaller
                successor = root
                root = root.left
            else:
                # Too small, must look in the right
                root = root.right
        return successor
