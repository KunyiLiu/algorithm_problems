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
        # left - right - root (postorder traversal)
        # BFS - queue not contanst extra space
        # DFS - have a space {height: last_node}, {0: Node_1, 1: Node_2, 2: Node_3}
        # if height exists, last_node.next = root.right
        # problem - how to utilize perfect tree, find the next node with same height?
        # two pointers: prev - for navigating down from root to leaf, cur - for level order traversal 
        if root is None:
            return root
        prev, cur = root, None 
        while prev.left:
            cur = prev 
            while cur:
                cur.left.next = cur.right 
                if cur.next:
                    cur.right.next = cur.next.left 
                cur = cur.next 
                
            prev = prev.left 
            
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # 'level_start' always points to the first node of the level we are currently ON
        level_start = root
        
        # If there's no left child, we are at the leaf level, so we stop
        while level_start.left:
            # 'curr' walks across the already-connected level_start level
            curr = level_start
            while curr:
                # 1. Connect children of the same parent
                curr.left.next = curr.right
                
                # 2. Connect the right child to the neighbor's left child
                if curr.next:
                    curr.right.next = curr.next.left
                
                # Move 'curr' to the right using the next pointer
                curr = curr.next
            
            # Move down to the next level's beginning
            level_start = level_start.left
            
        return root
        
