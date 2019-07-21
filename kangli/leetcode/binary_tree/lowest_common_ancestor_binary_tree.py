# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        left = right = None
        if root.left:
            left = self.lowestCommonAncestor(root.left, p, q)
        if root.right:
            right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right:
            return root 
        
        else:
            return left or right
        

'''
Success
Details 
Runtime: 88 ms, faster than 51.04% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Memory Usage: 26.3 MB, less than 38.39% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree.
Next challenges: Lowest Common Ancestor of a Binary Search Tree
'''
