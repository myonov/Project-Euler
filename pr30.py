from __future__ import print_function

def main():
    s = 0
    for i in range(10, 1000000):
        q = sum(map(lambda x: int(x)**5, str(i)))
        if q == i:
            s += q
    print(s)

if __name__ == '__main__':
    main()
