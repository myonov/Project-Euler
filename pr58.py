from __future__ import print_function

from pr3 import isprime

def main():
    p, c = 0, 1
    i = 2

    while True:
        d1 = i*i + 1

        d2 = d1 - i
        d3 = d1 + i

        p += sum([isprime(x) for x in [d1, d2, d3]])
        c += 4

#        print(i+1, p, c, float(p) / c)
        if float(p) / c < 0.1:
            print(i+1)
            break

        i += 2

if __name__ == '__main__':
    main()
