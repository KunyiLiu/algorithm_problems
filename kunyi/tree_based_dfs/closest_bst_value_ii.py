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
    
# Method 2
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
        # use to stack pre and suc to record the nodes 
        # in the path to target 
        # pre records the smaller nodes, while suc records the larger nodes 
        # two functions get_predecessor, get_successor 
        # time complexity O(h + k), space O(h)
        suc, pre, res = [], [], []
        while root:
            if root.val > target:
                suc.append(root)
                root = root.left 
            else:
                pre.append(root)
                root = root.right 

        for i in range(k):
            if len(pre) == 0 or (len(suc) != 0 and target - pre[-1].val > suc[-1].val - target):
                res.append(suc[-1].val)
                self.get_successor(suc)
            else:
                res.append(pre[-1].val)
                self.get_predecessor(pre)

                
        return res 
        
    def get_successor(self, stack):
        node = stack.pop()
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
            
    def get_predecessor(self, stack):
        node = stack.pop()
        if node.left:
            node = node.left
            while node:
                stack.append(node)
                node = node.right

# method 3 find the largest node closest to target, and then two pointers
# O(n)
    def closestKValues(self, root, target, k):
        if root is None or k == 0:
            return []
            
        nums = self.get_inorder(root)
        left = self.find_lower_index(nums, target)
        right = left + 1
        results = []
        for _ in range(k):
            if self.is_left_closer(nums, left, right, target):
                results.append(nums[left])
                left -= 1
            else:
                results.append(nums[right])
                right += 1
        return results
