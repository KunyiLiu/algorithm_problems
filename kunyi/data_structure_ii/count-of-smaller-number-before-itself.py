class Solution:
    """
    @param A: an integer array
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    class SegmentTreeNode:
        def __init__(self, start, end, count):
            self.start, self.end, self.count = start, end, count 
            self.left, self.right = None, None
        
    def countOfSmallerNumberII(self, A):
        # method: modify + query at the same time 
        # build segment tree from 0 to 10000
        result = []
        if len(A) == 0:
            return result 
        root = self.build(0, max(A))
        
        for a in A:
            res = 0
            if a > 0:
                res = self.query(root, 0, a-1)
            self.modify(root, a, 1)
            result.append(res)
            
        return result 
        
    def build(self, start, end):
        # return the root with the range from start to end
        if start > end:
            return None 
            
        if start == end:
            return SegmentTreeNode(start, end, 0)
            
        root = SegmentTreeNode(start, end)
        mid = (start + end) // 2 
        root.left = self.build(start, mid)
        root.right = self.build(mid+1, end)
        
        return root 
        
    def modify(self, root, num, count):
        # modify the count topdown
        # pay attention with root is None
        if root is None or root.start > num or num > root.end:
            return 
        
        root.count += count 
        mid = (root.start + root.end) // 2  
        if mid < num:
            self.modify(root.right, num, count)
        else:
            self.modify(root.left, num, count)
            
        return 
    
    def query(self, root, start, end):
        # have return - D & Q
        # return the count from start to end 
        if root.start > end or root.end < start:
            return 0 
            
        if start <= root.start and end >= root.end:
            # go to the lowest level
            return root.count 
            
        return self.query(root.left, start, end) + self.query(root.right, start, end)
            
        
        
