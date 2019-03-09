# 733 Given 2d array, starting coordinates, and new Color, color all cells 4-directionally connected to starting cell with newColor.
#Companies: Amazon(7), Google(3), Snapchat(2), Facebook(2), Zillow(2), Bloomberg(2), Uber.
# related topics Depth-first Search, Similar Questions: Island Perimeter.
# Hint 1: Write a recursive function that paints the pixel if it's the correct color, then recurses on neighboring pixels.


class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        color = image[sr][sc]
        self.dfs(image, sr, sc, color, newColor)
        return image

    def dfs(self, image, i, j, old_color, new_color):

        if 0 <= i <len(image) and 0 <= j <len(image[0]):
            if image[i][j] == old_color and image[i][j] != new_color:
                image[i][j] = new_color
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    self.dfs(image, i+dx, j+dy, old_color, new_color)
            return
        return

s = Solution()
print s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 3)
