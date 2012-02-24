from __future__ import print_function

def main():
    s = 1
    for x in range(1, 101):
        s *= x

    print(sum(map(int, str(s))))

if __name__ == '__main__':
    main()
