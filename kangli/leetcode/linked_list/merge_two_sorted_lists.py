# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next


'''
Success
Details
Runtime: 36 ms, faster than 97.29% of Python3 online submissions for Merge Two Sorted Lists.
Memory Usage: 13.8 MB, less than 5.06% of Python3 online submissions for Merge Two Sorted Lists.
Next challenges: Merge k Sorted Lists, Merge Sorted Array, Sort List, Shortest Word Distance II
'''
