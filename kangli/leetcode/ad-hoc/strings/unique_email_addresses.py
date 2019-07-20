class Solution:
    def numUniqueEmails(self, emails):
        counts = set()
        for email in emails:
            e = email.split("@")
            e[0] = e[0].split('+')[0]
            e = e[0].replace(".", "") + '@' + e[1]
            counts.add(e)
        return len(counts)


'''
Submission Result: Accepted
Next challenges: Add Binary, One Edit Distance, Shortest Palindrome
184 / 184 test cases passed.
Status: Accepted
Runtime: 40 ms
Memory Usage: 13.2 MB 
Your runtime beats 96.01 % of python3 submissions. 
Your memory usage beats 42.11 % of python3 submissions.

Related Topics: String
'''
