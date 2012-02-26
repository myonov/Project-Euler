from __future__ import print_function

def fib():
    yield 1
    yield 1
    a, b = 1, 1,
    while True:
        c = a + b
        yield c
        a, b = b, c

def main():
    for i, x in enumerate(fib()):
        if len(str(x)) == 1000:
            print(i+1)
            break

if __name__ == '__main__':
    main()
