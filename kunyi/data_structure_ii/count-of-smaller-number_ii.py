class Solution:
    """
    @param A: An integer array
    @param queries: The query list
    @return: The number of element in the array that are smaller that the given integer
    """
    class SegmentTreeNode:
        def __init__(self, start, end, count):
            self.start, self.end, self.count = start, end, count
            self.left, self.right = None, None
        
    def countOfSmallerNumber(self, A, queries):
        # interval search 
        # value from 0 to 10000
        root = self.build(0, 1000)

        for num in A:
            # nlog(n)
            self.modify(root, num, 1)
        
        print(root.start, root.end, root.count)
            
        result = []
        for query in queries:
            # mlog(n)
            result.append(self.query(root, 0, query-1))
            
        return result 
        
    def build(self, start, end):
        if start == end:
            return SegmentTreeNode(start, end, 0)
        if start > end:
            return None
        root = SegmentTreeNode(start, end, 0)
        mid = (start + end) // 2
        root.left = self.build(start, mid)
        root.right = self.build(mid+1, end) # mid+1 may larger than end
        return root 
        
    def modify(self, root, num, count):
        # corner case root is None
        if root is None or num < root.start or num > root.end:
            return 
        root.count += count 
        mid = (root.start + root.end) // 2
        if mid >= num:
            self.modify(root.left, num, count)
        else:
            self.modify(root.right, num, count)
        return 
    
    def query(self, root, start, end):
        if root is None or root.start > end or root.end < start:
            return 0 
        if start <= root.start and end >= root.end:
            return root.count 
            
        return self.query(root.left, start, end) + self.query(root.right, start, end)
            
