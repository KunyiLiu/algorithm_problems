# Method 1 backtracking
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        self.result = []
        if root is None:
            return self.result 
        self.helper(root, [])
        return self.result 
        
    def helper(self, root, subtree):
        if root is None:
            return 
        subtree.append(str(root.val))
        if root.left is None and root.right is None:
            self.result.append('->'.join(subtree))
            # return

        if root.left:
            self.helper(root.left, subtree)
            subtree.pop()
        
        if root.right:
            self.helper(root.right, subtree)
            subtree.pop()
        
        return
        
# Method 2: return tmp sublist from 0 to tmpLen 
"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        # write your code here
        result = []
        tmp = [0] * 100
        self.dfs(root, result, tmp, 0)
        return result
    
    def dfs(self, root, result, tmp, tmplen):
        if root is None:
            return 
        tmp[tmplen] = root.val
        tmplen += 1
        if root.left is None and root.right is None:
            #print(root.val, tmplen)
            for i in range(tmplen):
                if i == 0:
                    k = str(tmp[i])
                else:
                    k = k + '->' + str(tmp[i])
            result.append(k)
        self.dfs(root.left, result, tmp, tmplen)
        self.dfs(root.right, result, tmp, tmplen)
