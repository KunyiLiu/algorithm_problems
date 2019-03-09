class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, x):
        curMin = self.getMin()
        if curMin is None or x < curMin:
            curMin = x
        self.stack.append((x, curMin))

    # @return nothing
    def pop(self):
        self.stack.pop()

    def top(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[-1][0]

    def getMin(self):
        if len(self.stack) == 0:
            return None
        else:
            return self.stack[len(self.stack)-1][1]
