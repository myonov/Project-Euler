from __future__ import print_function

def main():
    l = [n*(3*n - 1) / 2 for n in range(1, 10000)]
    s = set(l)

    d = l[-1]

    for i in l:
        for j in l:
            if i+j in s and abs(i - j) in s:
                d = min(abs(i - j), d)

    print(d)

if __name__ == '__main__':
    main()
