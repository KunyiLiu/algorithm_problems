"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        # p in function keep the same?
        if root is None:
            return
        if p.val >= root.val:
            return self.inorderSuccessor(root.right, p)
        else:
            # if p < root, 
            # if left subtree exist then find in the right subtree
            # otherwize itself
            tmp = self.inorderSuccessor(root.left, p)
            if tmp:
                return tmp
            else:
                return root
