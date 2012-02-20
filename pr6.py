from __future__ import print_function

def main():
    n = 100
    r1 = sum((i * i for i in range(1, n+1)))
    r2 = sum((i for i in range(1, n+1))) ** 2
    print(r2 - r1)

if __name__ == '__main__':
    main()
