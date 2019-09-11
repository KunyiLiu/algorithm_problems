"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        # using merge sort 
        # find the median node by slow, fast pointer 
        if head is None:
            return
        if head.next is None:
            return head
        
        median = self.find_median(head)
        right = self.sortList(median.next)
        median.next = None
        left = self.sortList(head)
        root = self.merge(left, right)
        
        return root 
        
    def find_median(self, head):
        slow, fast = head, head 
        while fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        
        return slow
        
    def merge(self, left, right):
        if left is None:
            return right 
        if right is None:
            return left 
            
        dummy = ListNode(-1)
        root = dummy
        while left and right:
            if left.val < right.val:
                root.next = left 
                root = root.next 
                left = left.next 
            else:
                root.next = right 
                root = root.next 
                right = right.next 
                
        if left:
            root.next = left 
        if right:
            root.next = right 
            
        return dummy.next
