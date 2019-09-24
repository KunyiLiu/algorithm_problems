class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.timestamps = []  # keep it to length of 10
        self.messages = []
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        # similar to hit counter 
        # make a count (sorted timestamp, not sorted message)
        while len(self.timestamps) > 0 and timestamp - self.timestamps[0] >= 10:
            self.timestamps.pop(0)
            self.messages.pop(0)
        
        if message in self.messages:
            return False 
        else:
            self.timestamps.append(timestamp)
            self.messages.append(message)
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)

########  hashmap #########
class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = dict()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        #  self.messages : message: timestamp within 10 seconds
        if message not in self.messages:
            self.messages[message] = timestamp
            return True 
        
        if timestamp - self.messages[message] >= 10:
            self.messages[message] = timestamp
            return True 
        
        # already in self.messages - not updated
        return False 
