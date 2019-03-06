"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hashTable):
        # size/capacity > 0.1
        # about single linked list 
        if len(hashTable) == 0 or hashTable is None:
            return hashTable
        
        new_hash = [None] * len(hashTable) * 2 
        for item in hashTable:
            head = item
            while head is not None:
                self.addNode(new_hash, head.val)
                head = head.next 
                
        return new_hash
    
    def addNode(self, new_hash, num):
        size = num % len(new_hash)
        if new_hash[size] is None:
            new_hash[size] = ListNode(num)
        else:
            self.addList(new_hash[size], num)
    
    def addList(self, tail, num):
        if tail.next is not None:
            self.addList(tail.next, num)
        else:
            tail.next = ListNode(num)
