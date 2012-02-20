from __future__ import print_function

def isprime(x):
    if x == 2: return True
    if x == 3: return True
    if x % 2 == 0: return False
    i = 3
    while i*i <= x:
        if x % i == 0: return False
        i += 2
    return True

def main():
    num = 600851475143
    b = int(num ** 0.5 + 0.5)
    for s in range(b, 2, -1):
        if isprime(s) and num % s == 0:
            print(s)
            break

if __name__ == '__main__':
    main()
