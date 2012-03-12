from __future__ import print_function

def main():
    a = 0
    for i in range(1, 10):
        j = 1
        while True:
            r = len(str(i ** j))
            if r == j:
                a += 1
            if r < j:
                break
            j += 1
    print(a)

if __name__ == '__main__':
    main()
