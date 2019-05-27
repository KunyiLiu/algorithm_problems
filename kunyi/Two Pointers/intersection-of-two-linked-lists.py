"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """
    def getIntersectionNode(self, headA, headB):
        # write your code here
        pointer_a, pointer_b = headA, headB
        len_a, len_b = 0, 0
        while pointer_a is not None:
            len_a += 1 
            pointer_a = pointer_a.next 
            
        while pointer_b is not None:
            len_b += 1 
            pointer_b = pointer_b.next
        
        # make sure pointer_a and pointer_b start 
        # at the same steps from end 
        pointer_a, pointer_b = headA, headB
        while len_a > len_b:
            pointer_a = pointer_a.next
            len_a -= 1 
        while len_b > len_a:
            pointer_b = pointer_b.next
            len_b -= 1 
            
        while pointer_b is not None and pointer_a is not None:
            if pointer_a == pointer_b:
                return pointer_a
            pointer_a = pointer_a.next
            pointer_b = pointer_b.next 
            
        return 
