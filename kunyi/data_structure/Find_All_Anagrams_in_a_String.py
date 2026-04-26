class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # a sliding window with a fixed length
        s_len = len(s)
        p_len = len(p)
        if s_len < p_len:
            return []

        result = []
        # use [0] * 26 to calculate the substring char counter
        p_counter = [0] * 26
        s_counter = [0] * 26
        for i in range(p_len):
            p_counter[ord(p[i]) - ord('a')] += 1
            s_counter[ord(s[i]) - ord('a')] += 1

        if p_counter == s_counter:
            result.append(0)

        for i in range(1, s_len - p_len + 1):
            s_counter[ord(s[i-1]) - ord('a')] -= 1
            s_counter[ord(s[i + p_len - 1]) - ord('a')] += 1

            if s_counter == p_counter:
                result.append(i)

        return result
