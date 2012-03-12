from __future__ import print_function

from pr31 import memoize

def gcd(x, y):
    if x == 0: return y
    if y == 0: return x
    if x > y: return gcd(y, x%y)
    return gcd(x, y%x)

class RatException(Exception):
    pass

class Rat(object):
    def __init__(self, *args):
        l = len(args)
        if l == 2:
            self.p = args[0]
            self.q = args[1]
            self._red()
        elif l == 1:
            self.p = args[0]
            self.q = 1
        elif l == 0:
            self.p = 1
            self.q = 1
        else:
            raise RatException('Invalid rational')

    def __add__(self, other):
        p1 = self.p * other.q + self.q * other.p
        q1 = self.q * other.q
        return Rat(p1, q1)

    def __div__(self, other):
        return Rat(self.p * other.q, self.q * other.p)

    def _red(self):
        s = gcd(self.p, self.q)
        self.p /= s
        self.q /= s

    def __eq__(self, other):
        return self.p, self.q == other.p, other.q

    def __ne__(self, other):
        return not self == other

    def __hash__(self, other):
        return (self.p + 1001) ^ (self.q + 997)

    def __lt__(self, other):
        return self.p * other.q < other.p * self.q

    def __str__(self):
        return 'rat<{0} / {1}>'.format(self.p, self.q)

    __repr__ = __str__

@memoize
def x(nest):
    if nest == 0:
        return Rat(0)
    else:
        return Rat(1) / (Rat(2) + x(nest-1))

def main():
    limit = 1001
    Rat.count_ok = lambda x: len(str(x.p)) > len(str(x.q))
    a = 0

    for i in range(1, limit):
        if (Rat(1) + x(i)).count_ok():
            a += 1

    print(a)

if __name__ == '__main__':
    main()
