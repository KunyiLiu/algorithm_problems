####### use DFS to ensure the current first of the list, hard to update the ind ###
class NestedIterator(object):

    def __init__(self, nestedList):
        # use stack to record (Net, ind)
        # has_next: len(stack) > 0
        # next: dfs all the way until peak.isInteger is True 
        # pop the peak, and update the self.ind from record (Net, ind)
        self.stack = [(nestedList[0], 0)] 
        self.last_ind = 0
        
        
    # @return {int} the next element in the iteration
    def next(self):
        # add ind on the same level 
        # ind > len(same level), ind = last_net.ind + 1, than ind = 0 
        result = self.stack.pop()[0].getInteger()
        return result 
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        if len(self.stack) == 0:
            return False
        parent_net = self.stack[-1][0]
        tmp_ind = self.last_ind
        while not parent_net.isInteger():
            if tmp_ind < len(parent_net.getList()):
                parent_net = parent_net.getList()[tmp_ind]
                self.stack.append((parent_net, tmp_ind))
                tmp_ind = 0 
            else:
                _, current_ind = self.stack.pop()
                tmp_ind = current_ind + 1 
                if len(self.stack) == 0:
                    return False 
                    
                parent_net = self.stack[-1][0]
                    
        self.last_ind = self.stack[-1][1] + 1 
            
        return True



### 接枚举列表中的每个数字，然后将这些数字依次放到另一个数组中返回
class NestedIterator(object):

    def __init__(self, nestedList):
        self.next_elem = None
        self.stack = []
        for elem in reversed(nestedList):
            # [net3, net2, net1]
            self.stack.append(elem)
            
    # @return {int} the next element in the iteration
    def next(self):
        if self.next_elem is None:
            self.hasNext()
        temp, self.next_elem = self.next_elem, None
        return temp
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
    # time: O(N) - visit every item in the list, space: O(N)
        if self.next_elem:
            return True
            
        while self.stack:
            top = self.stack.pop()
            if top.isInteger():
                self.next_elem = top.getInteger()
                return True
            for elem in reversed(top.getList()):
                self.stack.append(elem)
        return False

##########
class NestedIterator(object):

    def __init__(self, nestedList):
        # use stack to record Net, use next_item to record the Net with isInteger is True 
        # hasNext - reversedly put Net to stack [Net3, Net2, Net1]
        # pop Net1, [Net3, Net2, Net1.2, Net1.1], if Net1.1 isInteger is True, pop and update next_item
        self.stack = nestedList
        self.next_item = None 
        
    # @return {int} the next element in the iteration
    def next(self):
        return self.next_item.getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        # Write your code here
        while len(self.stack) > 0:
            current_net = self.stack.pop()
            if current_net.isInteger():
                self.next_item = current_net
                return True 
                
            for net in reversed(current_net.getList()):
                self.stack.append(net)
                
        return False 

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
