from __future__ import print_function

def is_pal(r):
    return str(r) == str(r)[::-1]

def main():
    m = 0
    for s in range(100, 1000):
        for y in range(100, 1000):
            r = s*y
            if is_pal(r) and m < r:
                m = r
    print(m)

if __name__ == '__main__':
    main()
