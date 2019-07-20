# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        q = [root]
        depth = 0
        while q:
            size = len(q)
            depth +=1
            while size > 0:
                root = q.pop(0)
                size -= 1
                if root.left:
                    q.append(root.left)
                if root.right:
                    q.append(root.right)
        return depth


class Solution2:

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


'''
Success
Details 
Runtime: 68 ms, faster than 7.97% of Python3 online submissions for Maximum Depth of Binary Tree.
Memory Usage: 16.6 MB, less than 5.03% of Python3 online submissions for Maximum Depth of Binary Tree.
Next challenges: Balanced Binary Tree, Minimum Depth of Binary Tree, Maximum Depth of N-ary Tree
Related Topics: Tree, Depth-first Search
'''

'''
Submission Result: Accepted
Next challenges: Balanced Binary Tree, Minimum Depth of Binary Tree, Maximum Depth of N-ary Tree
'''
