######## O(1) - space revert linked list ########
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # Write your code here
        if head is None:
            return True

        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        # 1 -> 2 -> 3 -> 3 -> 2 -> 1 
        # 1 -> 2 -> 3 -> 3 <- 2 <- 1 
        #                  -> None
        p, last = slow.next, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next

        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next

        return p1 is None
        
### O(n) - space
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode.
    @return: A boolean.
    """
    def isPalindrome(self, head):
        # 1 -> 2 -> 3 -> 2 -> 1
        # O(n) - time/space
        length = 0
        node = head
        while node:
            length += 1 
            node = node.next 
        
        # if length is odd(5), reserve the first 5//2, jump one 
        # else even(6), reserve the first 6//2
        stack, count = [], 1
        while head:
            if length % 2 == 1 and count == (length // 2 + 1):
                head = head.next 
                count += 1 
                continue
            if count <= length // 2:
                stack.append(head.val)
            else:
                if len(stack) > 0 and head.val != stack.pop():
                    return False 
            head = head.next 
            count += 1 
            
        return True 
            
