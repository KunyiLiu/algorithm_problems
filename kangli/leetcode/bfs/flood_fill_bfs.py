from collections import deque

class Solution:
    def floodFill(self, image, sr, sc, newColor):
        queue = deque([(sr, sc)])
        oldColor = image[sr][sc]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        image[sr][sc] = newColor
        if oldColor == newColor: # otherwise while loop will never exit
            return image
        while queue:
            r, c = queue.popleft()
            for d in directions:
                nr, nc = r + d[0], c + d[1]
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]):
                    if image[nr][nc] == oldColor:
                        queue.append((nr, nc))
                        image[nr][nc] = newColor
        return image

'''
Submission Result: Accepted 
Next challenges: Zuma GameOut of Boundary PathsRecover a Tree From Preorder Traversal 

277 / 277 test cases passed.
Status: Accepted
Runtime: 64 ms
Memory Usage: 13.3 MB

Related Topics: Depth First Search (and BFS)
Similar Questions: Island Perimeter
'''
