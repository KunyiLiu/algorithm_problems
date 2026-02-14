class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        # exact reach => BFS, visited - farthest has jumped
        n = len(s)
        from collections import deque
        q = deque([])
        q.append(0)
        # used as visited hashset
        # Checking the farthest we have already visited, and avoid revisit
        farthest = 0

        while q:
            ind = q.popleft()

            # ensure the exploration within jump range for ind,
            # ensure only explore the ones > farthest
            start = max(ind + minJump, farthest + 1)
            end = min(ind + maxJump, n - 1)
            for j in range(start, end + 1):
                if s[j] == '0':
                    q.append(j)
                    if j == n - 1:
                        return True

            farthest = ind + maxJump

        return False
            
        

        
