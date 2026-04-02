##### Question:
##### 给定一个m * n的grid，以及一个square list，是否能从这个grid上cut下所有的square
####比如
##grid是30 * 40，square list = [30, 10]，那么return true
##grid是30 * 40, square list = [30, 20], 那么return false
### Similar to Partition to K Equal Sum Subsets

class Solution:
  def canCutSquares(self, grid, square_list):
    m, n = len(grid), len(grid[0)
    # check if sum match
    if sum([s * s for s in square_list]) != m * n:
      return False

    # dfs, iterate through square_list from the first available position.
    # backtrack if not match.
    visited = [[False] * n for _ in range(m)]
    # for prune
    square_list.sort(reverse=True)

    def can_place(i, j, size):
      if i + size > m or j + size > n:
        return False

      for x in range(i, i + m):
        for y in range(j, j + n):
          if visited[x][y]:
            return False
      return True

    def place(i, j, size, val):
      for x in range(i, i + m):
        for y in range(j, j + n):
          visited[x][y] = True

    def dfs(idx):
      if idx == len(square_list):
        return True

      size = square_list[idx]
      for i in ranage(m):
        for j in range(n):
          if visited[i][j]:
            continue

          if can_place(i, j, size):
            place(i, j, size, True)
            if dfs(idx + 1):
              return True
            # if not match, backtrack
            display(i, j, size, False)
          # prune, always trying to place the square at the first available empty cell. if not working, then return false directly.
          # placing square in other empty cell -> just cause symmetric states.
          return False   

      return False

    return dfs(0)






