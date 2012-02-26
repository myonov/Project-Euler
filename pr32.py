from __future__ import print_function

from itertools import permutations

def main():
    s = set()
    a = 0
    for p in permutations(range(1, 10)):
        for i in range(1, 10):
            for j in range(i+1, 9):
                n1 = int(''.join(map(str, p[:i])))
                n2 = int(''.join(map(str, p[i:j])))
                n3 = int(''.join(map(str, p[j:])))
                if n1 * n2 == n3 and n3 not in s:
                    a += n3
                    s.add(n3)

    print(a)

if __name__ == '__main__':
    main()
