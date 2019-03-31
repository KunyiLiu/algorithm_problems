"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    def searchRange(self, root, k1, k2):
        # write your code here
        import queue
        if root is None:
            return []
        queue = queue.Queue()
        queue.put(root)
        result = []
        
        while not queue.empty():
            node = queue.get()
            if node.val <= k2 and node.val >= k1:
                result.append(node.val)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)
                
        return result 
