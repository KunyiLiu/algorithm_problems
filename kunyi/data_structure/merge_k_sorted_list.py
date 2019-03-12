"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        # method 1: from bottom to up mergeKLists
        if len(lists) == 0 or lists is None:
            return 
        node = self.helper(lists, 0, len(lists) - 1)
        return node
        
    def helper(self, lists, start, end):
        if start == end:
            return lists[start]
        mid = start + (end - start) / 2
        left_node = self.helper(lists, start, mid)
        right_node = self.helper(lists, mid+1, end)
        node = self.merge2(left_node, right_node)
        return node 
        
    
    def merge2(self, l1, l2):
        dummy = ListNode(-1)
        head = dummy
        while l1 is not None and l2 is not None:
            if l1.val > l2.val:
                head.next = l2
                head = l2
                l2 = l2.next
            else:
                head.next = l1 
                head = l1 
                l1 = l1.next 
                
        head.next = l1 if l1 else l2 
        return dummy.next 
    
# method 2: heapq
"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node is not None:
                self.heapq_push_node(heap, node)
                
        dummy = ListNode(-1)
        head = dummy 
        while len(heap) > 0:
            _, target = heapq.heappop(heap)
            head.next = target
            head = head.next 
            if target.next:
                self.heapq_push_node(heap, target.next)
            
        return dummy.next 
        
    def heapq_push_node(self, heap, node):
        heapq.heappush(heap, (node.val, node))
