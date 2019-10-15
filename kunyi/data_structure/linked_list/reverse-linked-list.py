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

###### . recursive #####
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # bottom up
        if head is None:
            return
        if head.next is None:
            return head
        cur = self.reverseList(head.next)
        node = cur
        while node.next:
            node = node.next
        node.next = head
        head.next = None
        return cur
