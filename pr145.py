from __future__ import print_function

#runs about 3.5 hours
def main():
    limit = 1000000000
    a = 0

    for i in range(limit):
        if i % 10 == 0: continue
        k = int(str(i)[::-1])
        j = i + k
        if all(map(lambda x: x in ['1', '3', '5', '7', '9'], str(j))):
            a += 1

    print(a)

if __name__ == '__main__':
    main()
