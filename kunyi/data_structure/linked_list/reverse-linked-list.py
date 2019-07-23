"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        if head is None:
            return
        curr, last = head, None 
        while curr:
            next = curr.next 
            curr.next = last
            curr, last = next, curr 
        return last
