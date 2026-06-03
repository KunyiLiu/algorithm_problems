class Solution:
    def secondsToRemoveOccurrences(self, s: str) -> int:
        seconds = 0
        zeros = 0
        
        for char in s:
            if char == '0':
                zeros += 1
            elif zeros > 0: # It's a '1', and there are '0's before it
                # It takes at least `zeros` steps, or it gets delayed 
                # by the previous '1' (seconds + 1)
                seconds = max(seconds + 1, zeros)
                
        return seconds
