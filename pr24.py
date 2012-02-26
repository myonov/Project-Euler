from __future__ import print_function
from itertools import permutations

def main():
    r = permutations(range(10))
    for i, q in enumerate(r):
        if i == 1000000 - 1:
            print(''.join(map(str, q)))
            break

if __name__ == '__main__':
    main()
