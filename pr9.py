from __future__ import print_function

def main():
    for i in range(1, 1000):
        for j in range(1, 1000):
            k = 1000 - i - j
            if k <= 0: break
            s = sorted([i, j, k])
            if s[0] * s[0] + s[1] * s[1] == s[2] * s[2]:
                print(s[0]*s[1]*s[2])
                break

if __name__ == '__main__':
    main()
