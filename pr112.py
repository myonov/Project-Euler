from __future__ import print_function

def rel(n, f):
    n1 = str(n)
    l = len(n1)
    for i in range(l-1):
        if not f(n1[i], n1[i+1]): return False
    return True

up = lambda x, y: x <= y
down = lambda x, y: x >= y

def bouncy(n):
    return not rel(n, up) and not rel(n, down)

def main():
    a = 0
    b = 0
    while True:
        a += 1
        if bouncy(a):
            b += 1
        if float(b) / a >= 0.99:
            print(a)
            break

if __name__ == '__main__':
    main()
