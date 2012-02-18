from __future__ import print_function

def configurations(m, n):
    if n == 1:
        for x in range(1, m+1):
            yield [x]
    else:
        l = configurations(m, n-1)
        for y in l:
            for x in range(1, m+1):
                yield y + [x]

def main():
    total_pyramid = [0] * 37
    total_py = 4 ** 9

    total_cubic = [0] * 37
    total_cu = 6 ** 6

    for c in configurations(4, 9):
        total_pyramid[sum(c)] += 1

    for c in configurations(6, 6):
        total_cubic[sum(c)] += 1

    total_pyramid = [float(c) / total_py for c in total_pyramid]
    total_cubic = [float(c) / total_cu for c in total_cubic]

    prob = 0.0

    for i, v in enumerate(total_pyramid):
        for j, u in enumerate(total_cubic):
            if i > j:
                prob += v*u

    print("%0.7f" %prob)

if __name__ == '__main__':
    main()
