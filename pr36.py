from __future__ import print_function

def main():
    l = 1000001
    c = 0
    for i in range(1, l):
        b = bin(i)[2:]
        r = str(i)
        if b[::-1] == b and r == r[::-1]:
            c += i
    print(c)

if __name__ == '__main__':
    main()
