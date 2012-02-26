from __future__ import print_function

def main():
    s = 0

    l = 1001

    for i in range(1, l+1, 2):
        s += i*i

    for i in range(2, l, 2):
        s += 3*(i*i + 1)
    print(s)

if __name__ == '__main__':
    main()
