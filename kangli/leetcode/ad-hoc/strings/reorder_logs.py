class Solution:
    def reorderLogFiles(self, logs):
        letter_logs, res = [], []
        for log in logs:
            log_temp = log.split(" ")
            if log_temp[1].isdigit():
                res.append(log)
            else:
                letter_logs.append(log_temp)
        letter_logs = sorted(letter_logs, key=lambda x:(x[1:], x[0]))
        letter_logs = [" ".join(log) for log in letter_logs]
        return letter_logs+res


'''
Note: very similar to Amazon OA question (spring 2019)
Submission Result: Accepted
Next challenges: Validate IP Address, Reverse String II, Ambiguous Coordinates

62 / 62 test cases passed.
Status: Accepted
Runtime: 36 ms
Memory Usage: 13.2 MB

Related Topics: String
'''
