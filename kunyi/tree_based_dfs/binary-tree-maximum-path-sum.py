"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # bottom up method - helper(root) returns Max Downward Path starting at this node
        # Note! “What is the best path I can give to my parent?”
        # parent can only attach one side to keep the path valid.
        # Have self.result to get the max of all the Max Path Through This Node
        # Time: O(n)
        if root is None:
            return 0

        self.result = float('-inf')
        self.helper(root)

        return self.result

    def helper(self, root):
        if root is None:
            return 0

        left_max = max(self.helper(root.left), 0)
        right_max = max(self.helper(root.right), 0)

        self.result = max(self.result, root.val + left_max + right_max)

        # only choose 1 path upward
        return root.val + max(left_max, right_max)
