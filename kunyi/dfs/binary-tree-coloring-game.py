# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def find_node(self, root, x):
        if root is None:
            return
        
        if root.val == x:
            return root 
        
        left_root = self.find_node(root.left, x)
        if left_root:
            return left_root 
        right_root = self.find_node(root.right, x)
        if right_root:
            return right_root 
        
        return  
    
    def count_nodes(self, root):
        if root is None:
            return 0 
        
        left_count = self.count_nodes(root.left)
        right_count = self.count_nodes(root.right)
        return 1 + left_count + right_count
        
        
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        # first find root of x 
        # y can choose x_root.left, x_root.right, or the remaining nodes 
        # see if the number of nodes > n // 2 
        count_left, count_right = 0, 0
        x_root = self.find_node(root, x)
        if x_root:
            count_left = self.count_nodes(x_root.left)
            count_right = self.count_nodes(x_root.right)
        y_count = max(count_left, count_right, n - count_left - count_right - 1)
        return y_count > n // 2 
        
        
