################ topdown search, using self.result #####################
"""
Definition of SegmentTreeNode:
class SegmentTreeNode:
    def __init__(self, start, end, count):
        self.start, self.end, self.count = start, end, count
        # left/right child
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of segment tree.
    @param: start: start value.
    @param: end: end value.
    @return: The count number in the interval [start, end]
    """
    def query(self, root, start, end):
        # write your code here
        self.result = 0 
        if root is None or root.start > end or root.end < start:
            return 0
        self.helper(root, start, end)
        return self.result 
        
    def helper(self, root, start, end):
        if root is None:
            return 
        if (root.start == start and root.end == end) or (root.start == root.end):
            self.result += root.count
            return
        
        mid = (root.start + root.end) // 2
        if mid >= end:
            self.helper(root.left, start, end)
        elif mid < start:
            self.helper(root.right, start, end)
        else:
            self.helper(root.left, start, mid)
            self.helper(root.right, mid+1, end)
            
            
############### topdown search, bottom up addition ###################
class Solution:    
    # @param root, start, end: The root of segment tree and 
    #                          an segment / interval
    # @return: The count number in the interval [start, end] 
    def query(self, root, start, end):
        # write your code here
        if root is None:
            return 0

        if root.start > end or root.end < start:
            return 0
    
        if start <= root.start and root.end <= end:
            return root.count
        
        return self.query(root.left, start, end) + \
                   self.query(root.right, start, end)
