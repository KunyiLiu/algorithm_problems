# reset cur(pointer for the same layer) and dummy(to record the first node for the next layer), node(next layer)
# Time O(N), space O(1)
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        cur = dummy = Node()
        node = root
        while node:
            if node.left:
                cur.next = node.left
                cur = node.left
            if node.right:
                cur.next = node.right
                cur = node.right
            node = node.next
            if not node:
                node = dummy.next
                dummy.next = None # This is very important!!!
                cur = dummy # This is very important!!!
        return root
        
### recursive - find first node continuously ####
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # set first_node, and cur 
        # find the first_node
        # first_node -> next -> first_node 
        if root is None:
            return 
        
        first_node, cur = root, None
        while first_node:
            cur = first_node 
            first_node = self.construct_next_layer(cur, None)
            
        return root 
    
    def construct_next_layer(self, cur, visited):
        # if cur is None:
        #     return None
        node = None 
        while cur:
            if cur.left and cur.left != visited:
                node = cur.left
                break
            if cur.right and cur.right != visited:
                node = cur.right
                cur = cur.next
                break
            cur = cur.next 
        ## ERROR: node judgement
        if node:
            node.next = self.construct_next_layer(cur, node)
        return node 
