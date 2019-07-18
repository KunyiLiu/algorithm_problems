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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # method 1: first traversal to get the inorder list 
        # get the k-1 element from the list 
        # O(n)
        self.result = []
        self.inorder(root)
        return self.result[k-1]
        
    def inorder(self, root):
        if root is None:
            return 
        self.inorder(root.left)
        self.result.append(root.val)
        self.inorder(root.right)
        
        return 
        
        
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # Method 2: stack 中保存一路走到当前节点的所有节点
        # 如果当前点存在右子树，那么就是右子树中“一路向左”最左边的那个点
        # 如果当前点不存在右子树，则是走到当前点的路径中，shang一个左拐的点 pop 
        
        ## push node + all the way to left 
        ## O(h+k) h 是树的高度
        ## step 1. from root all the way to the left most leaf
        ## step 2. if poped node dont have right subtree, pop to the last layer 
        ##        else insert to the leftmost leaf of the right node 
        dummy = TreeNode(0)
        dummy.right = root 
        stack = [dummy]
        
        for i in range(k):
            # remove the smallest one
            node = stack.pop()
            if node.right:
                node = node.right 
                # inorder successor added to the very last 
                while node:
                    stack.append(node)
                    node = node.left 
                    
            if not stack:
                break 
            
        return stack[-1].val

############ current pointer + manual stack ############
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
    @param k: the given k
    @return: the kth smallest element in BST
    """
    def kthSmallest(self, root, k):
        # use stack simulate recursion
        stack = []
        current = root
        count = 0
        while len(stack) > 0 or current is not None:
            if current is not None:
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                count += 1 
                if count == k:
                    break
                current = current.right
                
        return current.val
            
