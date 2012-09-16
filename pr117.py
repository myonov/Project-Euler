from __future__ import print_function

def main():
    f = [0] * 100

    f[0] = f[1] = 1

    for x in range(2, 100):
        f[x] = f[x-1]

        if x >= 2:
            f[x] += f[x-2]

        if x >= 3:
            f[x] += f[x-3]

        if x >= 4:
            f[x] += f[x-4]

    print(f[50])

if __name__ == '__main__':
    main()
