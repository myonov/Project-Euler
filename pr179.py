from __future__ import print_function

def main():
    limit = 10 ** 7 + 1
    s = [2] * limit

    l = int(limit ** 0.5 + 1)

    for i in range(2, l):
        j = i * i
        s[j] -= 1
        while j < limit:
            s[j] += 2
            j += i

    ans = 0
    for i in range(2, limit-1):
        if s[i] == s[i+1]:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
