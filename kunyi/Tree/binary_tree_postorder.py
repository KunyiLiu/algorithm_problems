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
