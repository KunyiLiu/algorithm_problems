# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def levelOrder(self, root):
        if not root:
            return []
        res, queue = [], deque([root])
        while queue:
            temp = []
            qsize = len(queue)
            for i in range(qsize):
                cur = queue.popleft()
                temp.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            res.append(temp)
        return res


'''
Submission Result: Accepted
Next challenges: Binary Tree Zigzag Level Order Traversal, Binary Tree Level Order Traversal II,
Minimum Depth of Binary Tree, Binary Tree Vertical Order Traversal, Average of Levels in Binary Tree,
N-ary Tree Level Order Traversal, Cousins in Binary Tree
Share your acceptance!
'''
