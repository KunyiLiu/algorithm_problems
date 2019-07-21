"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A tree
    @return: buttom-up level order a list of lists of integer
    """
    def levelOrderBottom(self, root):
        # write your code here
        import Queue
        hash_table = {}
        result = []
        if root is None:
            return result 
            
        max_level = 0 
        queue = Queue.Queue()
        queue.put(root)
        while not queue.empty():
            max_level += 1 
            qsize = queue.qsize()
            for i in range(qsize):
                node = queue.get()
                if max_level not in hash_table:
                    hash_table[max_level] = []
                hash_table[max_level].append(node.val)
                
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
                    
        for i in range(max_level, 0, -1):
            result.append(hash_table[i])
            
        return result 
        
            
