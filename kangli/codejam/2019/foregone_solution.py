
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

t = int(raw_input()) # read a line with a single integer
for i in xrange(1, t + 1):
    N = raw_input()
    n, m = solve(N)
    print "Case #{}: {} {}".format(i, n, m)


'''
def solve(N):
    a, b = [], []
    for n in N:
        digits = generate_digits(n)
        a.append(digits[0][0])
        b.append(digits[0][1])
    a, b = int("".join(str(x) for x in a)), int("".join(str(y) for y in b))
    return a, b

def generate_digits(n):
    digits = []
    if n == '0':
        digits.append((0, 0))
    for i in range(1, int(n)):
        if i != 4 and int(n)-i != 4:
            digits.append((i, int(n)-i))
    return digits

# print solve('940')
t = 3
tests = [0, '4', '940', '4444']
for i in xrange(1, t + 1):
    N = tests[i]
    n, m = solve(N)
    print "Case #{}: {} {}".format(i, n, m)
'''
