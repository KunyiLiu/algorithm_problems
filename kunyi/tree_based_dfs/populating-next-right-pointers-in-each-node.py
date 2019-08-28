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
        
