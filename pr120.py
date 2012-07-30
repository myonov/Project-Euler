from __future__ import print_function

def main():
    limit = 1001
    s = 0

    for i in xrange(3, limit):
        s += 2 * i * ((i - 1) / 2) % (i * i)

    print(s)

if __name__ == '__main__':
    main()