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

 # single linked list 
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self._next = None

class LRUCache:
    """
    @param: capacity: An integer
    """

    def __init__(self, capacity):
        # head = dummy ->
        # have KeyToPrev hash table to record the previous node
        self.head = Node(0, 0)
        self.tail = self.head
        self.capacity = capacity
        self.KeyToPrev = {}
        
    def moveToTail(self, prev):
        # move the node the tail
        # prev -> node -> next -> ... -> tail
        # prev -> next -> ... -> tail -> node 
        # prev -> next ->  ... -> node (tail)
        node = prev._next 
        if self.tail == node:
            return 
        prev._next = node._next
        if node._next:
            self.KeyToPrev[node._next.key] = prev 
        node._next = None 
        self.tail._next = node
        self.KeyToPrev[node.key] = self.tail 
        self.tail = node 
        
        
    def popUpFront(self):
        node = self.head._next
        del self.KeyToPrev[node.key]
        self.head._next = node._next 
        self.KeyToPrev[self.head._next.key] = self.head
       

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        # write your code here
        if key not in self.KeyToPrev:
            return -1 
        prev = self.KeyToPrev[key]
        self.moveToTail(prev)
        # prev position has changed, so cannot use prev._next.value
        return  self.KeyToPrev[key]._next.value 

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        # write your code here
        if key in self.KeyToPrev:
            prev = self.KeyToPrev[key]
            prev._next.value = value 
            self.moveToTail(prev)
        else: 
            node = Node(key, value)
            self.tail._next = node 
            self.KeyToPrev[key] = self.tail 
            self.tail = node
            if len(self.KeyToPrev) > self.capacity:
                self.popUpFront()
