class Solution:
    def licenseKeyFormatting(self, S: str, K: int) -> str:
        res = []
        new_s = [c.upper() for c in S if c != '-']
        remainder = len(new_s) % K
        if remainder != 0:
            for i in range(remainder):
                res.append(new_s[i])
            if len(new_s) > 1:
                res.append('-')
        for j in range(len(new_s) - remainder):
            if j >= 1 and j % K == 0:
                res.append('-')
                res.append(new_s[j + remainder])
            else:
                res.append(new_s[j + remainder])
        return "".join(res)

'''
38 / 38 test cases passed.
Status: Accepted
Runtime: 76 ms
Memory Usage: 16.6 MB

Examples: 1) Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"
Explanation: The string S has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.

2) Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"
Explanation: The string S has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.
'''
