class Solution(object):
    def findLonelyPixel(self, picture):
        if not picture:
            return 0
        row_count = [0 for _ in range(len(picture))]
        col_count = [0 for _ in range(len(picture[0]))]

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    row_count[i] += 1
                    col_count[j] += 1
        count = 0
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and row_count[i] == 1 and col_count[j] == 1:
                    count += 1
        return count
