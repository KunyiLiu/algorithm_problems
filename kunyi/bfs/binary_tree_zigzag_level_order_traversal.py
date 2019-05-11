# DFS + Recursion
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        result = []
        self.preorder(root, 0, result)
        return result
        
    def preorder(self, root, level, result):
        if root is None:
            return
        if len(result) < level + 1:
            result.append([])  # create tmp
        if level % 2 == 0:
            result[level].append(root.val)
        else:
            result[level].insert(0, root.val)
        self.preorder(root.left, level + 1, result)
        self.preorder(root.right, level + 1, result)
        
# BFS
class Solution:
    """
    @param root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        
        import queue
        q = queue.Queue()
        order = 1 
        q.put(root)
        
        while not q.empty():
            tmp = []
            qsize = q.qsize()
            for i in range(qsize):
                node = q.get()
                tmp.append(node.val)
                if node.left:
                    q.put(node.left)
                if node.right:
                    q.put(node.right)
            if order == -1:
                result.append(tmp[::-1])
            else:
                result.append(tmp)
            order *= (-1)
                
        return result
