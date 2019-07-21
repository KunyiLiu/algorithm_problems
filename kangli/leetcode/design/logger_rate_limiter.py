class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._d = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """

        if message in self._d and timestamp - self._d[message] < 10:
            return False
        else:
            self._d[message] = timestamp
            return True
            
       
'''
Success
Details 
Runtime: 172 ms, faster than 5.23% of Python3 online submissions for Logger Rate Limiter.
Memory Usage: 19.6 MB, less than 5.10% of Python3 online submissions for Logger Rate Limiter.
Next challenges:
Design Hit Counter

Related Topics: Hash Table, Design
'''


class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.log = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        for i in range(10):
            if timestamp - i in self.log:
                if message in self.log[timestamp-i]:
                    return False 
        if timestamp not in self.log:
            self.log[timestamp] = [message]
        else:
            self.log[timestamp].append(message)
        return True      


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

'''
Success
Details 
Runtime: 204 ms, faster than 5.04% of Python3 online submissions for Logger Rate Limiter.
Memory Usage: 21.3 MB, less than 5.10% of Python3 online submissions for Logger Rate Limiter.
Next challenges:
Design Hit Counter
'''
