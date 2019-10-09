"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, sum):
        # backtracking + traverse (topdown)
        # contains negative elem?
        self.result = []
        self.dfs(root, [], sum)
        return self.result 
        
    def dfs(self, root, sub_result, tree_sum):
        if root is None:
            return 
        # Notice when root.left is None and root.right is None
        sub_result.append(root.val)
        if sum(sub_result) == tree_sum:
            self.result.append(sub_result[:])
            return
        if root.left:
            self.dfs(root.left, sub_result, tree_sum)
            sub_result.pop()
        if root.right:
            self.dfs(root.right, sub_result, tree_sum)
            sub_result.pop()
        
        return 

# BFS
class Solution:
    """
    @param root: a binary tree
    @param sum: the sum
    @return: the scheme
    """
    def pathSum(self, root, target):
        # iterative BFS (preorder traverse)
        # edge case: not exists/ null root 
        # 
        if root is None:
            return []
            
        queue = [(root, [root.val])]
        result = []
        while queue:
            node, path = queue.pop(0)
            if node.left is None and node.right is None and sum(path) == target:
                result.append(path)
                
            if node.left:
                queue.append((node.left, path + [node.left.val]))
            
            if node.right:
                queue.append((node.right, path + [node.right.val]))
        
        return result 
