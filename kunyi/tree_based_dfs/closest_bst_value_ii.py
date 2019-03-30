"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the given BST
    @param target: the given target
    @param k: the given k
    @return: k values in the BST that are closest to the target
    """
    def closestKValues(self, root, target, k):
        # max heap 
        # heap size > k, heapq.heappop(heap)
        import heapq 
        
        stack, heap = [], []
        while root:
            stack.append(root)
            root = root.left 
            
        while stack:
            node = stack[-1]
            heapq.heappush(heap, (-abs(node.val - target), node))
            if node.right:
                node = node.right 
                while node:
                    stack.append(node)
                    node = node.left 
            else: 
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()
                    
            if len(heap) > k:
                heapq.heappop(heap)
                
        result = [node.val for _, node in heap]
        return result[::-1]
