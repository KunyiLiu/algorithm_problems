class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # two pointers from start, end 
        # 
        if len(s) == 0:
            return []
        
        s.reverse()
        pos, cur = 0, 0 
        while pos < len(s):
            if s[pos] == ' ':
                s[cur:pos] = s[cur:pos][::-1]
                cur = pos + 1 
            pos += 1 
        s[cur:pos] = s[cur:pos][::-1]
