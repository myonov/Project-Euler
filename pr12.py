from __future__ import print_function

def get_divisors_count(n):
    i = 1
    cnt = 0
    while i*i < n:
        if n % i == 0:
            cnt += 2
        i += 1
    if i*i == n: cnt += 1
    return cnt

def main():
    s = 0
    i = 1
    while True:
        s += i
        g = get_divisors_count(s)
        if g > 500:
            print(s)
            break
        i += 1

if __name__ == '__main__':
    main()
