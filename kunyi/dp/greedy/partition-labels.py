class Solution:
    """
    @param S: a string
    @return: a list of integers representing the size of these parts
    """
    def partitionLabels(self, S):
        # first get the counter of chars in S
        # loop over S, char_set.add(first char)
        # substract count of char and add char to set until the set is null 
        # Time: O(n), Space: O(26)
        from collections import Counter
        if S is None or len(S) == 0:
            return []
            
        self.result = []
        char_count = Counter(S)
        self.helper(S, char_count, 0, set())
        return self.result 
        
    def helper(self, S, char_count, start, visited):
        if start >= len(S):
            return 
        
        for i in range(start, len(S)):
            visited.add(S[i])
            char_count[S[i]] -= 1 
            if char_count[S[i]] == 0:
                visited.remove(S[i])
            if len(visited) == 0:
                self.result.append(i - start + 1)
                break 
            
        self.helper(S, char_count, i + 1, visited)
        return 

##### use map to record the last ind of char 
class Solution(object):
    def partitionLabels(self, S):
        last = {c: i for i, c in enumerate(S)}
        right = left = 0
        ans = []
        for i, c in enumerate(S):
            right = max(right, last[c])
            if i == right:
                ans.append(i - left + 1)
                left = i + 1
            
        return ans
