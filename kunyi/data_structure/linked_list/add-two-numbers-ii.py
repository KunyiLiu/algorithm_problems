"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # O(m+n)
        # convert str/linked-list to num, reuslt from higher digit to lower
        # convert num to str, from lower to higher
        num1 = self.convert_num(l1)
        num2 = self.convert_num(l2)
        
        num = num1 + num2 
        dummy = ListNode(-1)
        if num == 0:
            return ListNode(0)
        while num:
            digit = num % 10 
            num = num // 10 
            node = ListNode(digit)
            tmp = dummy.next 
            dummy.next = node
            node.next = tmp 
            
        return dummy.next 
        
    def convert_num(self, head):
        if head is None:
            return 0 
            
        result = 0 
        while head:
            result = result * 10 + head.val
            head = head.next 
            
        return result 
