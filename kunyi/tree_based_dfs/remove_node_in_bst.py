"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: value: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, value):
        # write your code here
        if root is None:
            return 
        
        if root.val == value:
            if root.left is None:
                tmp = root.right
                # root = None
                return tmp 
                
            if root.right is None:
                tmp = root.left
                # root = None 
                return tmp 
            
            # get inorder successor and move it to the root 
            inorder_successor = self.get_successor(root.right)
            root.val = inorder_successor.val 
            # delete the successor 
            root.right = self.removeNode(root.right, inorder_successor.val)
 
        elif root.val > value:
            root.left = self.removeNode(root.left, value)
        else:
            root.right = self.removeNode(root.right, value)
            
        return root 
        
    def get_successor(self, root):
        result = None
        while root:
            result = root
            root = root.left
            
        return result
