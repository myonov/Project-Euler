from __future__ import print_function

def main():
    limit = 10000
    a = 0
    for i in range(10, limit):
        k = str(i)
        cnt = 0
        while cnt < 51:
            cnt += 1
            k1 = k[::-1]
            pal = str(int(k) + int(k1))
            if pal == pal[::-1]:
                break
            k = pal
        if cnt == 51:
            a += 1
    print(a)

if __name__ == '__main__':
    main()
