class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_1 = set()
        top_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        for c in top_row:
            row_1.add(c)
        row_2 = set()
        mid_row = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        for c in mid_row:
            row_2.add(c)
        row_3 = set()
        bottom_row = ["z", "x", "c", "v", "b", "n", "m"]
        for c in bottom_row:
            row_3.add(c)
        res = []
        for word in words: 
            a, b, c = 0, 0, 0
            for ch in word:
                if ch in row_1:
                    a = 1
                elif ch in row_2:
                    b = 1
                elif ch in row_3:
                    c = 1
            if a+b+c == 1:
                res.append(word)
        return res 


'''
Success
Details 
Runtime: 32 ms, faster than 84.71% of Python3 online submissions for Keyboard Row.
Memory Usage: 14 MB, less than 5.38% of Python3 online submissions for Keyboard Row.
Next challenges: Longest Substring with At Most Two Distinct Characters, Subarray Sums Divisible by K,
Time Based Key-Value Store
'''
