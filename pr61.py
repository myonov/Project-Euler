from __future__ import print_function

import sys

def main():
    funcs = [
        lambda n: n*(n + 1) / 2,
        lambda n: n*n,
        lambda n: n*(3*n - 1) / 2,
        lambda n: n*(2*n - 1),
        lambda n: n*(5*n - 3) / 2,
        lambda n: n*(3*n - 2),
    ]

    s = [set() for i in range(10, 100)]
    s2 = {}

    i = 1
    while True:
        if funcs[0](i) > 9999:
            break
        for j, f in enumerate(funcs):
            n = f(i)
            q = n % 100
            if 1000 > n or n > 9999 or q < 10:
                continue
            q = n / 100 % 100
            s[q-10].add(n)
            s2[n] = s2.get(n, []) + [j]

        i += 1

    def dfs(path, types):
        if len(path) == 6:
            q = path[-1] % 100 - 10
            if path[0] not in s[q]:
                return
            print(sum(path))
            sys.exit(0)
        p = path[-1]
        q = p % 100 - 10
        for l in s[q]:
            for t in s2[l]:
                if t not in types:
                    path.append(l)
                    types.append(t)
                    dfs(path, types)
                    path.pop()
                    types.pop()


    for k in s2:
        for t in s2[k]:
            dfs([k], [t])

if __name__ == '__main__':
    main()
