class Solution:
    def mostCommonWord(self, paragraph, banned):
        counts = {}
        punctuation = "!?',;."
        for p in punctuation:
            paragraph = paragraph.replace(p, " ")
        paragraph = paragraph.split(" ")
        max_freq, ans = 0, ""
        for word in paragraph:
            word = word.lower()
            if word in banned or word == "":
                continue
            else:
                counts[word] = 1 if word not in counts else counts[word] + 1
        for k, v in counts.items():
            if v > max_freq:
                max_freq = v
                ans = k
        return ans


'''
47 / 47 test cases passed.
Status: Accepted
Runtime: 44 ms
Memory Usage: 13.4 MB
Your runtime beats 36.82 % of python3 submissions
Your memory usage beats 5.67 % of python3 submissions. 

Related Topics: String
'''
