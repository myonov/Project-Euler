from __future__ import print_function

cards = [
    '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'
]

def groups(c):
    d = {}
    for k in c:
        d[k[0]] = d.get(k[0], []) + [k[1]]

    s = sorted(d.items(), key=lambda x: (-len(x[1]), -cards.index(x[0])))
    return s

def straight_flush(c):
    c = sorted(c, key=lambda x: -cards.index(x[0]))
    if straight(c) and flush(c):
        return True, c
    return False

def four_of_a_kind(c):
    d = groups(c)
    if len(d) == 2 and len(d[0][1]) == 4:
        l = []
        for i in d[0][1]:
            l.append((d[0][0], i))
        l.append((d[1][0], d[1][0][0]))
        return True, l
    return False

def full_house(c):
    d = groups(c)
    if len(d) == 2 and len(d[0][1]) == 3:
        l = []
        for i in d[0][1]:
            l.append((d[0][0], i))
        for i in d[1][1]:
            l.append((d[1][0], i))
        return True, l
    return False

def flush(c):
    c = sorted(c, key=lambda x: -cards.index(x[0]))
    if all(map(lambda x: x[1] == c[0][1], c)):
        return True, c
    return False

def straight(c):
    c = sorted(c, key=lambda x: -cards.index(x[0]))
    k = map(lambda x: cards.index(x[0]), c)

    i = 1
    while i < 5:
        if k[i-1] - 1 != k[i]:
            return False
        i += 1
    #in original poker however Ace can be 1
    return True, c

def three_of_a_kind(c):
    d = groups(c)
    if len(d[0][1]) == 3:
        l = []
        for i in d[0][1]:
            l.append((d[0][0], i))
        l.append((d[1][0], d[1][0][0]))
        l.append((d[2][0], d[2][0][0]))
        return True, l
    return False

def two_pairs(c):
    d = groups(c)
    if len(d[0][1]) == 2 and len(d[1][1]) == 2:
        l = []
        for i in d[0][1]:
            l.append((d[0][0], i))

        for i in d[1][1]:
            l.append((d[1][0], i))
        l.append((d[2][0], d[2][0][0]))
        return True, l
    return False

def pair(c):
    d = groups(c)
    if len(d[0][1]) == 2:
        l = []
        for i in d[0][1]:
            l.append((d[0][0], i))

        for k in d[1:]:
            for i in k[1]:
                l.append((k[0], i))
        return True, l
    return False

def high_card(c):
    c = sorted(c, key=lambda x: -cards.index(x[0]))
    return True, c

def cmp(c1, c2):
    funcs = [
        straight_flush, four_of_a_kind, full_house, flush,
        straight, three_of_a_kind, two_pairs, pair, high_card
    ]

    ind = [len(funcs), len(funcs)]
    cs = []

    for i, c in enumerate([c1, c2]):
        for j, f in enumerate(funcs):
            res = f(c)
            if res:
                ind[i] = j
                cs.append(res[1])
                break

    if ind[0] < ind[1]:
        return 1
    if ind[0] > ind[1]:
        return -1

    for i in range(5):
        ci1 = cards.index(cs[0][i][0])
        ci2 = cards.index(cs[1][i][0])

        if ci1 < ci2:
            return -1
        if ci1 > ci2:
            return 1

    return 0 #draw

def main():
    a = 0
    for line in open('poker.txt', 'r'):
        cards = map(lambda x: (x[0], x[1]), line.strip().split())
        c1 = cards[:5]
        c2 = cards[5:]
        if cmp(c1, c2) > 0:
            a += 1

    print(a)

if __name__ == '__main__':
    main()
