# BFS 
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # travese 2^h - 1
        import Queue
        result = []
        if root is None:
            return result
        queue = Queue.Queue()
        queue.put(root)
        while not queue.empty():
            tmp = []
            qsize = queue.qsize()
            for i in range(qsize):
                node = queue.get()
                tmp.append(node.val)
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
                    
            result.append(tmp)
            
        return result
        
 # DFS
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
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        # write your code here
        result = []
        if root is None:
            return result
        targetlevel = 0
        while 1:
            tmp = []
            curlevel = 0
            self.dfs(root, tmp, curlevel, targetlevel)
            # if there are not element in a level
            if tmp == []:
                break
            result.append(tmp)
            targetlevel += 1
        return result
    
    def dfs(self, root, tmp, curlevel, targetlevel):
        if root is None or curlevel > targetlevel:
            return
        if curlevel == targetlevel:
            tmp.append(root.val)
            return
        self.dfs(root.left, tmp, curlevel + 1, targetlevel)
        self.dfs(root.right, tmp, curlevel + 1, targetlevel)
