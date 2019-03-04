# double linked list
class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self._next = None
        

class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        # do intialization if necessary
        self.capacity = capacity
        self.data_set = {}
        self.head = Node()
        self.tail = Node()
        self.head._next = self.tail 
        self.tail.prev = self.head
        
    def addToHead(self, node):
        node._next = self.head._next
        self.head._next = node 
        node.prev = self.head
        node._next.prev = node 
        
    def deleteNode(self, node):
        node.prev._next = node._next
        node._next.prev = node.prev
        

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.data_set:
            return - 1 
        node = self.data_set[key]
        self.deleteNode(node)
        self.addToHead(node)
        return node.value 

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        node = Node(key, value)
        if key not in self.data_set:
            self.addToHead(node)
        else:
            existing_node = self.data_set[key]
            self.deleteNode(existing_node)
            self.addToHead(node)
        self.data_set[key] = node 
        
        if len(self.data_set.keys()) > self.capacity:
            del self.data_set[self.tail.prev.key]
            self.deleteNode(self.tail.prev)
