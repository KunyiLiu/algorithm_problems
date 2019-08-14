"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        from collections import deque 
        if not root:
            return 0
        queue = deque([root])
        depth = 0
        while queue:
            qsize = len(queue)
            for i in range(qsize):
                node = queue.popleft()
                for child in node.children:
                    queue.append(child)
            depth += 1 
        return depth


'''
Success
Details 
Runtime: 656 ms, faster than 41.80% of Python3 online submissions for Maximum Depth of N-ary Tree.
Memory Usage: 95.3 MB, less than 8.33% of Python3 online submissions for Maximum Depth of N-ary Tree.
Next challenges: Delete Node in a BST, Freedom Trail, Binary Tree Pruning
'''
