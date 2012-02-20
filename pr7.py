from __future__ import print_function

def isprime(x):
    i = 3
    while i*i <= x:
        if x % i == 0: return False
        i += 2

    return True

def main():
    i = 5
    s = 2
    while True:
        if isprime(i):
            s += 1
            print(str(s) + ' ' + str(i))
        if s == 10001:
            print(i)
            break
        i += 2

if __name__ == '__main__':
    main()
