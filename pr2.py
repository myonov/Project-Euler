from __future__ import print_function

def fib():
    f1, f2 = 1, 1
    yield f1
    yield f2
    while 1:
        yield f1 + f2
        f1, f2 = f2, f1 + f2

def main():
    s = 0
    for x in fib():
        if x > 4000000: break
        if x % 2 == 0: s += x
    print(s)

if __name__ == '__main__':
    main()

