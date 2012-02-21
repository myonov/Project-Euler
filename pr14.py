from __future__ import print_function

def main():
    m = 0
    for i in range(2, 1000000):
        q = i
        c = 0
        while q != 1:
            if q % 2 == 0:
                q = q / 2
            else:
                q = q * 3 + 1
            c += 1
        if m < c:
            m = c
            r = i
    print(r)

if __name__ == '__main__':
    main()
