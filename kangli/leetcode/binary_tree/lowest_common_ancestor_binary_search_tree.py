# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if not all([root, p, q]):
            return None
        min_val, max_val = min(p.val, q.val), max(p.val, q.val)
        
        while root:
            if min_val <= root.val <= max_val:
                return root
            elif min_val > root.val:
                root = root.right
            elif max_val < root.val:
                root = root.left


'''
Success
Details 
Runtime: 84 ms, faster than 79.52% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Memory Usage: 18 MB, less than 5.84% of Python3 online submissions for Lowest Common Ancestor of a Binary Search Tree.
Next challenges:
Balanced Binary Tree
Find Mode in Binary Search Tree
Construct Binary Tree from String
'''
