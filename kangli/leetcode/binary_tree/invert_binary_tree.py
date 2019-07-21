# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        from collections import deque
        q = deque([root])
        while q:
            cur_root = q.popleft()
            if cur_root:
                cur_root.right, cur_root.left = cur_root.left, cur_root.right
                q.append(cur_root.left)
                q.append(cur_root.right)
        return root


'''
Success
Details 
Runtime: 40 ms, faster than 15.35% of Python3 online submissions for Invert Binary Tree.
Memory Usage: 13.8 MB, less than 5.07% of Python3 online submissions for Invert Binary Tree.
Next challenges:
Find Mode in Binary Search Tree
Add One Row to Tree
Maximum Binary Tree II
'''
