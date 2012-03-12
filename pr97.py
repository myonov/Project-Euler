from __future__ import print_function

from pr48 import pow_10

def main():
    limit = 7830457
    m = 28433

    x = pow_10(limit, 2)
    x = (m * x + 1) % (10 ** 10)
    print(x)

if __name__ == '__main__':
    main()
