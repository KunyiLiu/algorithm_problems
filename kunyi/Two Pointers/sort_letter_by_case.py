class Solution:
    """
    @param: chars: The letter array you should sort by Case
    @return: nothing
    """
    def sortLetters(self, chars):
        # partition
        if chars is None or len(chars) == 0:
            return ''
            
        start, end = 0, len(chars) - 1 
        while start <= end:
            while start <= end and ord(chars[start]) >= 97:
                start += 1 
                
            while start <= end and ord(chars[end]) < 97:
                end -= 1 
                
            if start <= end:
                chars[start], chars[end] = chars[end], chars[start]
                start += 1 
                end -= 1 
                
        return chars
