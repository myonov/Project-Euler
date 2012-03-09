from __future__ import print_function

def main():
    s = {}
    limit = 5
    for i in range(1, 10000):
        n = i ** 3
        sn = str(n)
        q = tuple((x, sn.count(str(x))) for x in range(10))

        r = s.get(q, (0, n))
        r1 = (r[0]+1, r[1] if r[1] < n else n)
        s[q] = r1

        if r1[0] == 5:
            print(r1[1])
            break

if __name__ == '__main__':
    main()
