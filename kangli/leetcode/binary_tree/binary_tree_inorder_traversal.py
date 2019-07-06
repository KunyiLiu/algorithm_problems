# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        res, stack = [], []
        while root or stack:
            if root:
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                res.append(root.val)
                root = root.right
        return res

class Solution:
    def inorderTraversalRecursive(self, root: TreeNode) -> List[int]:
        res = []
        self.inorder_recurse(root, res)
        return res

    def inorder_recurse(self, root, res):
        if not root:
            return
        if root.left:
            self.inorder_recurse(root.left, res)
        res.append(root.val)
        if root.right:
            self.inorder_recurse(root.right, res)


'''
Next challenges: Validate Binary Search Tree, Binary Tree Preorder Traversal, Binary Tree Postorder Traversal,
Binary Search Tree Iterator, Kth Smallest Element in a BST, Closest Binary Search Tree Value II,
Inorder Successor in BSTConvert Binary Search Tree to Sorted Doubly Linked List, Minimum Distance Between BST Nodes

Related Topics: Hash Table, Stack, Tree 
Similar Questions: Similar Questions
Validate Binary Search TreeBinary Tree Preorder Traversal, Binary Tree Postorder Traversal, Binary Search Tree Iterator,
Kth Smallest Element in a BSTClosest Binary Search Tree Value II,
Inorder Successor in BST, Convert Binary Search Tree to Sorted Doubly Linked List, Minimum Distance Between BST Nodes
'''
