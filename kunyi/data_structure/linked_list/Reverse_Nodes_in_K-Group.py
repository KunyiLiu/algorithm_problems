#######  Space: O(n)#####

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # reference: reorder linked list
        # Step 1: split k node linked list + remaining (n- k)
        # step 2: reverse(first k); step 3: merge
        # continue the process on the 
        dummy = ListNode()
        dummy.next = head
        cur = head
        nodes = []
        while cur:
            nodes.append(cur)
            cur = cur.next

        prev = dummy
        n = len(nodes)
        for i in range(n):
            if (i + 1) % k == 0:
                nodes[i].next = None
                self.reverse(nodes[i - k + 1])
                # now the nodes[i - k + 1] becomes tail, and nodes[i] becomes head
                prev.next = nodes[i]
                prev = nodes[i - k + 1]

        # attach the remaining nodes
        if n % k != 0:
            prev.next = nodes[-(n % k)]

        return dummy.next

    def reverse(self, head):
        # it guarantees there is k nodes from head forward
        last, cur = None, head
        while cur:
            nxt = cur.next
            cur.next = last
            last = cur
            cur = nxt


# Space: O(1) ####

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        groupPrev = dummy

        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next

            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


