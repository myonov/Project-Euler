from __future__ import print_function

def pow_10(n, x):
    if n == 1:
        return x
    if n % 2 == 0:
        s = pow_10(n/2, x) % (10**10)
        return s * s % (10**10)
    else:
        return x * pow_10(n-1, x) % (10**10)

def main():
    s = 0
    for i in range(1, 1001):
        s = (s + pow_10(i, i)) % (10**10)
    print(s)

if __name__ == '__main__':
    main()
