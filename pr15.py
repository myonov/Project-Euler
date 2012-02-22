from __future__ import print_function

def main():
    d = [[0 for x in range(21)] for x in range(21)]
    for i in range(21):
        d[0][i] = 1
        d[i][0] = 1

    for i in range(1, 21):
        for j in range(1, 21):
            d[i][j] = d[i-1][j] + d[i][j-1]

    print(d[i][j])

if __name__ == '__main__':
    main()
