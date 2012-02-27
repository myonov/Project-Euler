from __future__ import print_function

def main():
    fact = [1]
    for i in range(1, 10):
        fact.append(fact[-1]*i)

    l = 1000001
    s = 0

    for i in range(3, l):
        j = sum(map(lambda x: fact[int(x)], str(i)))
        if i == j:
            s += i

    print(s)

if __name__ == '__main__':
    main()
