######################### TIME lIMIT EXCEED ######################
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # write your code here
        bigger, smaller = head, None 
        while bigger is not None:
            smaller = bigger
            bigger = bigger.next 
            # if bigger < smaller, return False 
            tmp_pointer = head
            len_smaller, len_bigger = 0, 0
            while tmp_pointer != bigger:
                len_bigger += 1 
                if tmp_pointer == smaller:
                    break
                tmp_pointer = tmp_pointer.next 
            else:
                return True
            
        return False
        
#################### Floyd's Cycle Detection ################
class Solution:
    """
    @param head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        # Floyd
        # Traverse linked list using two pointers.  Move one pointer by one and other pointer by two. 
        # If these pointers meet at same node then there is a loop.  If pointers do not meet then linked
        # list doesn’t have loop.
        bigger, smaller = head, head 
        if head is None:
            return False
        while True:
            if bigger.next is not None:
                bigger = bigger.next.next
                smaller = smaller.next
                if bigger is None:
                    return False
                if bigger == smaller:
                    return True 
            else:
                return False
