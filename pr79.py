from __future__ import print_function

def main():
    d = {}
    cnt = [0 for i in range(10)]

    for l in open('keylog.txt', 'r'):
        l = l.strip()
        for i in range(3):
            dig = ord(l[i]) - ord('0')
            d[dig] = d.get(dig, 0) + i
            cnt[dig] += 1.0

    for k in d:
        d[k] = d[k] / float(cnt[k])

    d = sorted(d.items(), key=lambda x: (x[1], x[0]))
    print(''.join(map(lambda x: str(x[0]), d)))

if __name__ == '__main__':
    main()
