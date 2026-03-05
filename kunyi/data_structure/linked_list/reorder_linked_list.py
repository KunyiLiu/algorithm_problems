class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # NOTE: not modify, recorder (move)
        # create node list, and use inbound two pointers
        # Time complexity: O(n), Space: O(n)
        if not head:
            return

        nodes = []
        cur = head

        while cur:
            nodes.append(cur)
            cur = cur.next

        i, j = 0, len(nodes) - 1
        # inbound two pointers
        while i < j:
            nodes[i].next = nodes[j]
            i += 1
            if i >= j:
                break

            nodes[j].next = nodes[i]
            j -= 1

        nodes[i].next = None


####  O(1) Space - use fast/slow pinters #####
### 1. split; 2. reverse the latter; 3. merge #####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        # 1. find middle
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 2. reverse second half
        prev = None
        cur = slow.next
        slow.next = None

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        # 3. merge
        first, second = head, prev
        while second:
            t1 = first.next
            t2 = second.next

            first.next = second
            second.next = t1

            first = t1
            second = t2
