class Solution:
    def uncommonFromSentences(self, A, B):
        A, B, a_words, b_words = A.split(" "), B.split(" "), {}, {}
        res = []
        for word in A:
            a_words[word] = 1 if word not in a_words else a_words[word] + 1

        for word in B:
            b_words[word] = 1 if word not in b_words else b_words[word] + 1

        for k, v in a_words.items():
            if v == 1 and k not in b_words:
                res.append(k)

        for k, v in b_words.items():
            if v == 1 and k not in a_words:
                res.append(k)
        return res


'''
Related Topics: Hash Table

Success
Details
Runtime: 36 ms, faster than 81.68% of Python3 online submissions for Uncommon Words from Two Sentences.
Memory Usage: 13.2 MB, less than 41.33% of Python3 online submissions for Uncommon Words from Two Sentences.
Next challenges:
Bulls and Cows
Subdomain Visit Count
Verifying an Alien Dictionary
'''
