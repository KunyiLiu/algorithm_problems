######### RECURSION O(N) #######

"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        root, is_incre = self.helper(head)
        if is_incre:
            tmp = root
            root = ListNode(1, next=tmp)
            
        return root 
        
    def helper(self, head):
        # def: return head after plus
        # if head.next is None:
        #     return Node(val + 1), is_incre
        #  tmp, is_incre = self.plusOne(head.next)
        # if is_incre: head.val = 
        # return head
        if head is None:
            return head, False 
            
        node, is_inc = self.helper(head.next)
        if node is None or is_inc:
            # ERROR. note when use the same shorted if else continuously
            if head.val == 9:
                head.val = 0
                is_inc = True
            else:
                head.val += 1 
                is_inc = False
        
        return head, is_inc
        
####### iterative #####
## dummy before head - addition carry, l - the last digit which is not 9, r - the last digit 
class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        dummy = ListNode(0)
        dummy.next = head
        l = dummy
        r = dummy
        while r.next != None:
            r = r.next
            if r.val != 9:
                l = r
        
        if r.val != 9:
            r.val += 1;
        else:
            l.val += 1
            l = l.next
            while l != None:
                l.val = 0
                l = l.next
        
        if  dummy.val == 0:
            return dummy.next
        
        return dummy;
