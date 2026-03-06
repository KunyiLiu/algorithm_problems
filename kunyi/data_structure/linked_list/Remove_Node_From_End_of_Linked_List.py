# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # traverse to get nodes list
        # => total m nodes, target is 4 - 2 index node to remove
        # make target - 1's next = target's next
        # if no target - 1, then return None
        if not head:
            return None

        total = 0
        cur = head
        while cur:
            total += 1
            cur = cur.next

        if total < n:
            return None

        target_ind = total - n

        if target_ind == 0:
            return head.next

        cur = head
        for i in range(total - 1):
            if (i + 1) == target_ind:
                cur.next = cur.next.next
                break

            cur = cur.next

        return head
        
