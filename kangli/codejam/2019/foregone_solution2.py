def solve(N):
    a, b = [], []
    for n in N:
        digits = generate_digits(n)
        a.append(digits[0])
        b.append(digits[1])
    a, b = int("".join(str(x) for x in a)), int("".join(str(y) for y in b))
    return a, b

def generate_digits(n):
    lookup = {
        '0':['0', '0'],
        '1':['0', '1'],
        '2':['1', '1'],
        '3':['1', '2'],
        '4':['2', '2'],
        '5':['2', '3'],
        '6':['3', '3'],
        '7':['2', '5'],
        '8':['3', '5'],
        '9':['3', '6']
    }
    return lookup[n]

t = 3
tests = [0, '4', '940', '4444']
for i in xrange(1, t + 1):
    N = tests[i]
    n, m = solve(N)
    print "Case #{}: {} {}".format(i, n, m)
