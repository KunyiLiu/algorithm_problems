# recursion
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # write your code here
        self.result = []
        self.helper(root)
        return self.result 
        
    def helper(self, root):
        if root is None:
            return 
        
        self.helper(root.left)
        self.result.append(root.val)
        self.helper(root.right)
        
        return 

    
# iteration
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Inorder in ArrayList which contains node values.
    """
    def inorderTraversal(self, root):
        # stack record the path of nodes that lead to node (not includes node)
        result, stack = [], []
        if root is None:
            return result 
        node = root 
        while node:
            stack.append(node)
            node = node.left 
        
        while stack:
            node = stack[-1]
            result.append(node.val) 
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
                
        return result 
