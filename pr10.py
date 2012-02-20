from __future__ import print_function

prime_list = [2]

def gen_primes(n):
    for x in range(3, n, 2):
        l = len(prime_list)
        f = True
        i = 0
        while i < l:
            if prime_list[i] * prime_list[i] > x:
                break
            if x % prime_list[i] == 0:
                f = False
                break
            i += 1

        if f:
            prime_list.append(x)

    return prime_list

def main():
    print(sum(gen_primes(2000000)))

if __name__ == '__main__':
    main()
