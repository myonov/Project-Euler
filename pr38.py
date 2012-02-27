from __future__ import print_function

def main():
    m = 0
    for i in range(1, 100000):
        s = ''
        j = 1
        while len(s) < 9:
            s = s + str(i*j)
            j += 1
        if len(s) > 9: continue
        if len(set(list(s))) == 9 and '0' not in s:
            m = max(m, int(s))
    print(m)

if __name__ == '__main__':
    main()
