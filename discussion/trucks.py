def minimumDistance(numRows, numColumns, area):
    # WRITE YOUR CODE HERE
    visited = [[False] * numColumns for i in range(numRows)]
    visited[0][0] = True
    queue = [(0, 0)]
    result = 0
    delta_X = [1, -1, 0, 0]
    delta_Y = [0, 0, 1, -1]
    while len(queue) > 0:
        qsize = len(queue)
        for i in range(qsize):
            x, y = queue.pop(0)
            print("x {} y {}".format(x, y))

            if area[x][y] == 9:
                return result
                # up down
            for j in range(4):
                new_x, new_y = x + delta_X[j], y + delta_Y[j]
                if 0 <= new_x < numRows and 0 <= new_y < numColumns and not visited[new_x][new_y] and area[new_x][
                    new_y]:
                    queue.append((new_x, new_y))
                    visited[new_x][new_y] = True
        print('queue {}'.format(queue))

        result += 1

    return -1


print(minimumDistance(4, 4, [[1, 1, 1, 1],
                             [0, 0, 1, 1],
                             [0, 0, 1, 1],
                             [9, 1, 1, 1]])
      )
