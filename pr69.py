from __future__ import print_function

def compute_func():
    from pr10 import gen_primes
    limit = 1000001
    pr = gen_primes(limit)
    s = set(pr)

    def phi(n):
        n1 = n
        i = 0
        res = 1

        if n == 2:
            return 1

        if n == 3:
            return 2

        while pr[i] * pr[i] <= n:
            alpha = 0
            while n1 % pr[i] == 0:
                alpha += 1
                n1 /= pr[i]
            if alpha > 0:
                res *= pr[i] ** (alpha - 1) * (pr[i] - 1)
            if n1 in s:
                res *= (n1-1)
                break
            i += 1
        return res
    return phi

def main():
    phi = compute_func()

    limit = 1000001
    mx = 0.0
    ans = 0

    for i in range(2, limit):
        q = float(i) / phi(i)
        #print(i, q)
        if q > mx:
            mx = q
            ans = i

    print(ans)

if __name__ == '__main__':
    main()
