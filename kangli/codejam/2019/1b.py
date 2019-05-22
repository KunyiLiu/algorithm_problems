
def manhattan_crepe(array, solve, t):
    x, y, d = array[0], array[1], array[2]
    x_dict, y_dict = {}, {}
    if d == 'N':
        y += 1
    if d == 'S':
        y -= 1
    if d == 'E':
        x += 1
    if d == 'W':
        x -= 1
    x_dict[x] = 1 if x not in x_dict else x_dict[x]+1
    y_dict[y] = 1 if y not in y_dict else y_dict[y]+1
    if solve:
        x_max = max(x_dict, key=x_dict.get)
        y_max = max(y_dict, key=y_dict.get)
        for k, v in x_dict.items():
            if v == x_dict[x_max]:
                if k < x_max:
                    x_max = k
        for k, v in y_dict.items():
            if v == y_dict[y_max]:
                if k <y_max:
                    y_max = k

        print( "Case #{}: {} {}".format(t, x_max, y_max))

# manhattan_crepe([2, 4, 'N'], False, 1)
# manhattan_crepe([2, 6, 'S'], False, 1)
# manhattan_crepe([1, 5, 'E'], False, 1)
# manhattan_crepe([3, 5, 'W'], True, 1)

t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    p, q = [int(s) for s in raw_input().split(" ")]
    for j in range(p):
        a = []
        x, y, d = [s for s in raw_input().split(" ")]
        a.extend([int(x), int(y), str(d)])
        if j == p-1:
            manhattan_crepe(a, True, i)
        else:
            manhattan_crepe(a, False, i)
