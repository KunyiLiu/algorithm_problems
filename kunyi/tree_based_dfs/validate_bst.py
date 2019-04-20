"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
# recursion + min/max of subtree
class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # use d&q method 
        # ensure left tree and right tree is Valid
        # then root.left < root < roo.right
        result, _, _ = self.dfs(root)
        return result
        
    def dfs(self, root):
        if root is None:
            return True, None, None
        
        left_valid, leftmin, leftmax = self.dfs(root.left)
        right_valid, rightmin, rightmax = self.dfs(root.right)
        if left_valid and right_valid:
            if leftmax and rightmin:
                is_valid = root.val > leftmax and root.val < rightmin
                rootmin = min(root.val, leftmin, rightmin)
                rootmax = max(root.val, leftmax, rightmax)
            elif leftmax:
                is_valid, rootmin, rootmax = root.val > leftmax, min(root.val, leftmin),\
                max(root.val, leftmax)
            elif rightmin:
                 is_valid, rootmin, rootmax = root.val < rightmin, min(root.val, rightmin),\
                max(root.val, rightmax)
            else:
                is_valid, rootmin, rootmax = True, root.val, root.val
        
            return is_valid, rootmin, rootmax
        return False, None, None
    
# method 2 recursion + last_val
    def isValidBST(self, root):
        self.is_bst = True
        self.lastval = None
        self.helper(root)
        return self.is_bst
        
    def helper(self, root):
        if root is None:
            return 
        self.helper(root.left)
        if self.lastval and self.lastval >= root.val:
            self.is_bst = False
            return
        self.lastval = root.val
        self.helper(root.right)

# method 3: iterator
     """
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        # write your code here
        if root is None:
            return True 
            
        last_node, node = None, root 
        stack = []
        
        while node is not None:
            stack.append(node)
            node = node.left 
            
        last_node = stack[-1]
        # stack - record the path to node (not includes node)
        while stack:
            node = stack[-1]
            if node.right:
                node = node.right 
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
                    
            if stack:
                # compare the previous and current last_node
                if stack[-1].val <= last_node.val:
                    return False
                last_node = stack[-1]
                
        return True 
