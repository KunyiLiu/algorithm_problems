"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

Example of iterate a tree:
iterator = BSTIterator(root)
while iterator.hasNext():
    node = iterator.next()
    do something for node 
"""


class BSTIterator:
    """
    @param: root: The root of binary tree.
    """
    def __init__(self, root):
        # push and all the way to left 
        self.stack = []
        self.cur = root 
        

    """
    @return: True if there has next node, or false
    """
    def hasNext(self, ):
        # write your code here
        return len(self.stack) > 0 or self.cur is not None

    """
    @return: return next node
    """
    def next(self, ):
        # from the beginneing, O(h) 
        # but on avg, the time is O(1)
        while self.cur is not None:
            self.stack.append(self.cur)
            self.cur = self.cur.left 
            
        node = self.stack.pop()
        nxt = node 
        self.cur = node.right 
        return nxt
