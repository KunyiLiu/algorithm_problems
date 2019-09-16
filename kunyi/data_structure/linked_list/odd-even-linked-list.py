"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: a singly linked list
    @return: Modified linked list
    """
    def oddEvenList(self, head):
        # odd.next = even.next 
        if head is None:
            return 
        
        odd_head, even_head = ListNode(-1), ListNode(-1)
        
        odd, even = odd_head, even_head
        count = 1
        while head:
            # Error head.next will change
            head_next = head.next
            if count % 2 == 1:
                odd.next = head 
                odd = odd.next
            elif count % 2 == 0:
                even.next = head 
                even = even.next
            
            head = head_next
            count += 1
        
        even.next = None 
        odd.next = even_head.next 
        
        return odd_head.next
