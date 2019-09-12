"""
Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = nextDefinition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        # traverse binary tree using current pointer and stack 
        # first set up a dummy node 
        # create DoublyListNode
        if root is None:
            return
        
        dummy = DoublyListNode(-1)
        node = dummy
        stack, cur = [], root 
        while len(stack) > 0 or cur:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur_node = DoublyListNode(cur.val)
                node.next, node.prev = cur_node, cur_node
                node = cur_node
                cur = cur.right 
                
        return dummy.next
