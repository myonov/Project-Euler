from __future__ import print_function

from pr57 import Rat

def main():
    e = [1, 2, 1]
    limit = 101

    for i in range(3, limit):
        e.append(1)
        e.append(e[-3] + 2)
        e.append(1)

    end = 98

    i = end - 1
    r = Rat(e[end])

    while i >= 0:
        r = Rat(e[i]) + Rat(1) / r
        i -= 1

    r = Rat(2) + Rat(1) / r

    print(sum(map(int, str(r.p))))

if __name__ == '__main__':
    main()
