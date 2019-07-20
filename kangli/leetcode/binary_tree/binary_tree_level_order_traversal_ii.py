# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        queue, res = collections.deque([(root, 0)]), []
        while queue:
            node, level = queue.popleft()
            if node:
                if len(res) < level+1:
                    res.insert(0, [])
                res[-(level+1)].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res



'''
Success
Details 
Runtime: 44 ms, faster than 57.40% of Python3 online submissions for Binary Tree Level Order Traversal II.
Memory Usage: 14.1 MB, less than 8.32% of Python3 online submissions for Binary Tree Level Order Traversal II.
Next challenges: Average of Levels in Binary Tree

Related Topics: Tree, Breadth-first Search
'''
