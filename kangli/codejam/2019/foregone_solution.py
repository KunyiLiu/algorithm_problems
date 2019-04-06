


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
