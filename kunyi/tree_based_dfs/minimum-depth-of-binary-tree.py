"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # DQ, similar to max depth of binary tree
        if root is None:
            return 0 
        
        # note: {1,#,2,3}, when one child is None, calculate the child of other side 
        if root.left is None:
            return self.minDepth(root.right) + 1 
        if root.right is None:
            return self.minDepth(root.left) + 1 
            
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        height = min(left, right) + 1 
        
        return height
        
        
######## iterative #######
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        # top-down traverse
        if root is None:
            return 0 
        queue = [root]
        height = 1
        while len(queue) > 0:
            qsize = len(queue)
            for i in range(qsize):
                node = queue.pop(0)
                if node.left is None and node.right is None:
                    return height
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            height += 1 
            
        return height
