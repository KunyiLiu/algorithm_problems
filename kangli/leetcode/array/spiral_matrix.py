class Solution(object):
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        result = []
        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1

        while l <= r and t <= b:

            for i in range(l, r + 1):
                result.append(matrix[l][i])
            t += 1

            for i in range(t, b + 1):
                result.append(matrix[i][r])
            r -= 1

            if t <= b:
                for i in range(r, l - 1, -1):
                    result.append(matrix[b][i])
                b -= 1

            if l <= r:
                for i in range(b, t - 1, -1):
                    result.append(matrix[i][l])
                l += 1
        return result
