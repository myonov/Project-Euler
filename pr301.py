from __future__ import print_function

def main():
    limit = 2 ** 30 + 1

    a = 0

    for x in range(1, limit):
        if x ^ (2 * x) ^ (3 * x) == 0:
            a += 1

    print(a)

if __name__ == '__main__':
    main()