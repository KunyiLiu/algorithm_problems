# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root or self.helper(root.left, root.right):
            return True
        else:
            return False

    def helper(self, left, right):
        if not left or not right:
            return left == right
        if left.val != right.val:
            return False
        return self.helper(left.left, right.right) and self.helper(left.right, right.left)


'''
Submission Result: Accepted
Next challenges: Diameter of Binary TreeRedundant Connection IIInsufficient Nodes in Root to Leaf Paths
Share your acceptance!
'''
