from __future__ import print_function

def main():
    limit = 1000 / 2
    c = {}
    for h in range(1, limit):
        for j in range(h):
            for k in range(h):
                if j + k > h and j*j + k*k == h*h:
                    p = j + k + h
                    c[p] = c.get(p, 0) + 1

    print(max((c[k], k) for k in c)[1])

if __name__ == '__main__':
    main()
