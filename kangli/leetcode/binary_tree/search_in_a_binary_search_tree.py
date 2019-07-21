# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        while root:
            if root.val == val:
                return root
            elif root.val < val:
                root = root.right
            elif root.val > val:
                root = root.left
        return None
        
        
'''
Success
Details 
Runtime: 84 ms, faster than 58.76% of Python3 online submissions for Search in a Binary Search Tree.
Memory Usage: 15.7 MB, less than 5.85% of Python3 online submissions for Search in a Binary Search Tree.
Next challenges:
Insert into a Binary Search Tree

Related Topics: Tree
Similar Questions: Closest Binary Search Tree Value, Insert into a Binary Search Tree
'''
