####  O(N^2) #####
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""

        self.result = ""
        for mid in range(len(s)):
            self.helper(s, mid, mid)
            self.helper(s, mid, mid + 1)

        return self.result

    def helper(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        if (right - 1) - (left + 1) + 1 > len(self.result):
            self.result = s[left + 1 : right] 

##    manacher algorithm ######

class Solution:
    def longestPalindrome(self, s: str) -> str:
        # manacher: "ababd" (n) -> #a#b#a#b#d# (2n + 1)
        # l (left boundary), r (right bound), P to record radius (not consider center)
        # i is the selected center.
        # p[i] = min(r - i, P[mirror_i if mirror_i is withint boundary])

        t = '#' + '#'.join(s) + '#'
        n = len(t)
        l, r = 0, 0
        P = [0 for _ in range(n)]

        for i in range(n):
            # if there is any mirror, update the at least radium
            if i < r:
                P[i] = min(r - i, P[l + r - i])

            # expand outwards from i no matter if i is within (l, r)
            while i >= P[i] + 1 and i + P[i] + 1 < n and t[i - P[i] - 1] == t[i + P[i] + 1]:
                P[i] += 1

            if i + P[i] > r:
                l, r = i - P[i], i + P[i]

        max_len, center_ind = max((v, i) for i, v in enumerate(P))
        # remove #
        start_ind = (center_ind - max_len) // 2
        return s[start_ind : start_ind + max_len]


