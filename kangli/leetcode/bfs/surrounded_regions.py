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
