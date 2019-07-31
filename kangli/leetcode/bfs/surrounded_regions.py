# 7/30 redo
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        from collections import deque 
        queue = deque([])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == len(board)-1) or (j==0 or j == len(board[0])-1):
                    if board[i][j] == 'O':
                        queue.append((i, j))
        while queue:
            r, c = queue.popleft()
            directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
            board[r][c] = 'S'
            for d in directions:
                nr, nc = d[0] + r, d[1] + c 
                if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == 'O':
                    queue.append((nr, nc))
                    board[nr][nc] = 'S'
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'
                    
                    
'''
Success
Details 
Runtime: 168 ms, faster than 40.68% of Python3 online submissions for Surrounded Regions.
Memory Usage: 14.4 MB, less than 67.60% of Python3 online submissions for Surrounded Regions.
Next challenges:
Number of Islands
Walls and Gates
'''


# 7/6/19 redo
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        m, n = len(board), len(board[0])
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == 'O':
                    self.bfs(board, i, j)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                if board[i][j] == 'W':
                    board[i][j] = 'O'

    def bfs(self, board, sr, sc):
        from collections import deque
        queue = deque([(sr, sc)])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        m, n = len(board), len(board[0])
        board[sr][sc] = 'W'
        while queue:
            r, c = queue.popleft()
            for d in directions:
                nr, nc = d[0] + r, d[1] + c
                if 0 <= nr < m and 0 <= nc < n and board[nr][nc] == 'O':
                    board[nr][nc] = 'W'
                    queue.append((nr, nc))
'''

59 / 59 test cases passed.
Status: Accepted
Runtime: 124 ms
Memory Usage: 14.2 MB
64.85% runtime and 79.62% memory
'''

class Solution(object):
    def solve(self, board):
        q = collections.deque([])
        for r in range(len(board)):
            for c in range(len(board[0])):
                if r == 0 or r == len(board)-1 or c == 0 or c == len(board[0])-1:
                    if board[r][c] == 'O':
                        q.append((r, c))
        while q:
            r, c = q.popleft()
            if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 'O':
                board[r][c] = 'S'
                q.append((r+1, c)); q.append((r-1, c))
                q.append((r, c+1)); q.append((r, c-1))
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'

'''
Success
Details
Runtime: 156 ms, faster than 45.92% of Python online submissions for Surrounded Regions.
Memory Usage: 16.9 MB, less than 12.26% of Python online submissions for Surrounded Regions.
Next challenges:
Course Schedule II
Remove Invalid Parentheses
Regions Cut By Slashes

Related Topics: Depth-first Search, Breadth-first Search, Union Find 
Similar Questions: Number of Islands, Walls and Gates
'''
