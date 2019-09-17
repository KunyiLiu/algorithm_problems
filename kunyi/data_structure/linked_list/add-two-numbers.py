"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def addLists(self, l1, l2):
        # l1 would be null? 
        num1 = self.convert_num(l1)
        num2 = self.convert_num(l2)
        
        num = num1 + num2 
        dummy = ListNode(-1)
        head = dummy
        if num == 0:
            return ListNode(0)
        while num:
            digit = num % 10 
            num = num // 10 
            head.next = ListNode(digit)
            head = head.next 
            
        return dummy.next 
        
    def convert_num(self, head):
        if head is None:
            return 0 
            
        nums = []
        while head:
            nums.insert(0, head.val)
            head = head.next 
            
        result = 0 
        for num in nums:
            result = result * 10 + num 
            
        return result 
    
############ or simulate addition ######
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        ptr = head
        carry  = 0
        while True:
            if l1 != None:
                carry += l1.val
                l1 = l1.next
            if l2 != None:
                carry += l2.val
                l2 = l2.next
            ptr.val = carry % 10
            carry /= 10
            # 运算未结束新建一个节点用于储存答案，否则退出循环
            if l1 != None or l2 != None or carry != 0:
                ptr.next = ListNode(0)
                ptr = ptr.next
            else: 
                break
        return head
