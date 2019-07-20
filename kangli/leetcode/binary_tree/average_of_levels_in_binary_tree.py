# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque 
class Solution:
    def averageOfLevels(self, root):
        q, res = deque([root]), []
        while q:
            temp = []
            for i in range(len(q)):
                node = q.popleft()
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(sum(temp)/len(temp))
        return res
                    
                    
'''
Success
Details 
Runtime: 56 ms, faster than 86.47% of Python3 online submissions for Average of Levels in Binary Tree.
Memory Usage: 16.2 MB, less than 23.08% of Python3 online submissions for Average of Levels in Binary Tree.
Next challenges: Serialize and Deserialize N-ary Tree, Complete Binary Tree Inserter, Range Sum of BST

Related Topics: Tree
Similar Questions: Binary Tree Level Order Traversal, Binary Tree Level Order Traversal II
'''
