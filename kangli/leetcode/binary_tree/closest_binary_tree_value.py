# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        res = root.val
        while root:
            if abs(target-root.val) < abs(target-res):
                res = root.val
            if target < root.val:
                root = root.left
            else:
                root = root.right
        return res 


'''
Success
Details 
Runtime: 40 ms, faster than 94.02% of Python3 online submissions for Closest Binary Search Tree Value.
Memory Usage: 15.7 MB, less than 5.42% of Python3 online submissions for Closest Binary Search Tree Value.
'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        sorted_arr = []
        self.inorder(root, sorted_arr)
        min_diff = 2**32-1
        ans = 0 
        for n in sorted_arr:
            if abs(n-target) < min_diff:
                min_diff = abs(n-target)
                ans = n
        return ans 
    
    def inorder(self, root, res):
        if not root:
            return
        self.inorder(root.left, res)
        res.append(root.val)
        self.inorder(root.right, res)
        
'''
Time and Space: O(N) (tree traversal), O(1)
Success
Details 
Runtime: 48 ms, faster than 61.90% of Python3 online submissions for Closest Binary Search Tree Value.
Memory Usage: 15.7 MB, less than 6.41% of Python3 online submissions for Closest Binary Search Tree Value.
Next challenges:
Count Complete Tree Nodes
Closest Binary Search Tree Value II
Search in a Binary Search Tree

Related Topics: Binary Search, Tree
'''
