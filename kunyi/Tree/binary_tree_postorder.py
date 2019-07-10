# Push the root node to the first stack.
# Pop a node from the first stack, and push it to the second stack.
# Then push its left child followed by its right child to the first stack.
# Repeat step 2) and 3) until the first stack is empty.
# Once done, the second stack would have all the nodes ready to be traversed in post-order. Pop off the nodes from the second stack one by one and you’re done.


class Solution:
    """
    @param: root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # write your code here
        result = []
        stack = []
        rev_stack = []
        if root is None:
            return result
        stack.append(root)
        while len(stack) > 0:
            node = stack.pop()
            rev_stack.append(node)
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
        while len(rev_stack) > 0:
            node = rev_stack.pop()
            result.append(node.val)
            
        return result
    
######### reverse of root right left, similar to preorder###############
class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # reserve - root right left
        current = root
        result, stack, reverse_result = [], [], []
        while len(stack) > 0 or current is not None:
            if current:
                reverse_result.append(current.val)
                stack.append(current)
                current = current.right
            else:
                current = stack.pop()
                current = current.left 
                
        return reverse_result[::-1]
    
    #############3 recursion ###################
    class Solution:
    """
    @param root: A Tree
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        # reserve - root right left
        result = []
        self.helper(root, result)
        return result
        
    def helper(self, root, result):
        # traverse top down 
        if root is None:
            return 
        self.helper(root.left, result)
        self.helper(root.right, result)
        result.append(root.val)
        return 
