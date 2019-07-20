# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if (p and not q) or (q and not p):
            return False
        if p.val != q.val:
            return False
        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

'''
Submission Result: Accepted 
Next challenges: Populating Next Right Pointers in Each Node II, 
Verify Preorder Sequence in Binary Search Tree, Binary Tree Cameras
'''
