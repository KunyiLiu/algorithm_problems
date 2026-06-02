"""
No extra space usage
"""
class Solution:
    def compress(self, chars: List[str]):
        if len(chars) == 0:
            return 0

        # k as write pointer, i as read pointer, j as another read pointer for finding
        # duplicates
        i = j = k = 0
        n = len(chars)
        while i < n:
            chars[k] = chars[i]
            k += 1 
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1 
            # chars i .. j - 1 are the same
            if j - i > 1:
                for c in str(j - i):
                    chars[k] = c
                    k += 1

            i = j

        return k
