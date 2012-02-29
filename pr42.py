from __future__ import print_function

def main():
    s = set()
    a = 0

    for i in range(1, 1000):
        a += i
        s.add(a)

    words = [w.replace('"', '') for w in open('words.txt').read().split(',')]

    a = 0
    for w in words:
        q = sum(map(lambda x: ord(x) - ord('A') + 1, w))
        if q in s:
            a += 1
    print(a)

if __name__ == '__main__':
    main()
