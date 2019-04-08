def make_path(path):
    my_path = []
    for c in path:
        if c == 'E':
            my_path.append('S')
        else:
            my_path.append('E')
    return "".join(x for x in my_path)

t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    n = int(raw_input())
    path = raw_input()
    my_path = make_path(path)
    print("Case #{}: {}".format(i, my_path))

#works passed all 3 test sets
