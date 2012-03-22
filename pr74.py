from __future__ import print_function

def main():
    fact = [1, 1]
    for i in range(2, 10):
        fact.append(fact[-1] * i)

    def chain(n):
        r = [n]
        while True:
            s = sum(map(lambda x: fact[int(x)], str(n)))
            if s in r:
                return len(r)
            r.append(s)
            n = s

    limit = 1000001
    cnt = 0
    for i in range(limit):
        if chain(i) == 60:
            cnt += 1

    print(cnt)

if __name__ == '__main__':
    main()
