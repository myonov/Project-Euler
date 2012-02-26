from __future__ import print_function

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]
    return wrapper

def main():

    c = [1, 2, 5, 10, 20, 50, 100, 200]
    cl = len(c)

    @memoize
    def f(s, h):
        if s == 0: return 1
        q = 0
        for j in range(cl):
            if s - c[j] >= 0 and c[j] >= h:
                q += f(s-c[j], c[j])
        return q

    print(f(200, 0))

if __name__ == '__main__':
    main()
