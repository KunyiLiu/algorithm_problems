######### Time: O(n), space: O(n)  traverse ######

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the given tree
    @return: the values of the nodes you can see ordered from top to bottom
    """
    def rightSideView(self, root):
        # bfs on tree (acyclic)
        # last elem of the layer
        result = []
        if root is None:
            return result
        queue = [root]
        while len(queue) > 0:
            qsize = len(queue)
            for i in range(qsize):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(node.val)
                
        return result 
