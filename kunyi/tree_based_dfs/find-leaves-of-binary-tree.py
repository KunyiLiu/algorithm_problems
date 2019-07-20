"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: collect and remove all leaves
    """
    from collections import defaultdict
    level_hash = defaultdict(list)
    def findLeaves(self, root):
        # write your code here
        result = []
        height = self.dfs(root)
        for i in range(1, height + 1):
             result.append(self.level_hash[i])
        return result 
        
    def dfs(self, root):
        # get max depth
        if root is None:
            return 0
        height = max(self.dfs(root.left), self.dfs(root.right))+1 
        self.level_hash[height].append(root.val)
        return height
