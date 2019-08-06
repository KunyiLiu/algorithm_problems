class Solution:
    def numEnclaves(self, A: List[List[int]]) -> int:
        from collections import deque 
        queue = deque([])
        count = 0 
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    count += 1
                if (i == 0 or j == 0 or i == len(A)-1 or j == len(A[0])-1) and A[i][j] == 1:
                    queue.append((i, j))          
        while queue:
            r, c = queue.popleft()
            A[r][c] = 2
            count -= 1
            for d in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                nr, nc = r+d[0], c+d[1]
                if 0 <= nr < len(A) and 0<= nc <len(A[0]) and A[nr][nc] == 1 and (nr, nc) not in queue:
                    A[nr][nc] = 2 
                    queue.append((nr, nc))
        return count  


'''
Success
Details 
Runtime: 684 ms, faster than 34.09% of Python3 online submissions for Number of Enclaves.
Memory Usage: 14.9 MB, less than 46.15% of Python3 online submissions for Number of Enclaves.
Next challenges: Validate Binary Search Tree, Increasing Order Search Tree, Unique Paths III
'''
