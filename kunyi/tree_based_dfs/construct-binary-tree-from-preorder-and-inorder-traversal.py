"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param preorder : A list of integers that preorder traversal of a tree
    @param inorder : A list of integers that inorder traversal of a tree
    @return : Root of a tree
    """
    def buildTree(self, preorder, inorder):
        # 前序的第一个为根，在中序中找到根的位置。
        # 中序中根的左右两边即为左右子树的中序遍历。同时可知左子树的大小size-left。
        # 前序中根接下来的size-left个是左子树的前序遍历。
        # 由此可以递归处理左右子树。
        # Remeber one structure: preorder: root - whole left subtree - whole right subtree 
        # inorder: whole left sub - root - whole right
        if len(preorder) == 0 or len(inorder) == 0:
            return 
        # 0,..., root_index - 1 left subtree
        # root_index + 1, ... right subtree
        root_index = inorder.index(preorder[0])
        root = TreeNode(preorder[0])
        root.left = self.buildTree(preorder[1:1+root_index], inorder[:root_index])
        root.right = self.buildTree(preorder[1+root_index:], inorder[1+root_index:])
        return root 
