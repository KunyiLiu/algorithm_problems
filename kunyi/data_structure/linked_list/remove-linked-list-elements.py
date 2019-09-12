"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a ListNode
    @param val: An integer
    @return: a ListNode
    """
    def removeElements(self, head, val):
        # set up dummy, in case the first node is val, return dummy.next 
        # last, cur 
        # if cur is val, update next_node, last.next = cur.next 
        if head is None:
            return 
        
        dummy = ListNode(-1, head)
        last, cur = dummy, head 
        while cur:
            if cur.val == val:
                 # last not move
                last.next = cur.next 
            else:
                last = last.next 
            cur = last.next 
            
        return dummy.next
