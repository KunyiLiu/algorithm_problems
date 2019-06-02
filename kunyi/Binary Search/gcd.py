# Euclidean Algorithm
def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


if __name__ == '__main__':
    print('The {} and {} gcd is {}'.format(12, 1, gcd(12, 1)))
    print('The {} and {} gcd is {}'.format(60, 48, gcd(60, 48)))
    print('The {} and {} gcd is {}'.format(48, 60, gcd(48, 60)))
