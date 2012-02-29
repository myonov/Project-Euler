from __future__ import print_function
from itertools import permutations

from pr3 import isprime

def main():
    m = None
    for x in range(7, 0, -1):
        for p in permutations(range(1, x+1)):
            num = int(''.join(map(str, p)))
            if isprime(num):
                m = max(m, num)
    print(m)

if __name__ == '__main__':
    main()
