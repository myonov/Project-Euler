from __future__ import print_function

def main():
    s1, s2, s3 = set(), set(), set()

    start_t = 285 + 1
    start_p = 165 + 1
    start_h = 143 + 1
    limit = lambda x: x + 100001

    for i in range(start_t, limit(start_t)):
        s1.add(i*(i+1) / 2)
    for i in range(start_p, limit(start_p)):
        s2.add(i*(3*i-1) / 2)
    for i in range(start_h, limit(start_h)):
        s3.add(i*(2*i-1))

    s = s1.intersection(s2.intersection(s3))
    print(min(s))

if __name__ == '__main__':
    main()
