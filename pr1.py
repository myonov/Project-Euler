from __future__ import print_function

def main():
    print(sum(filter(lambda x: x % 3 == 0 or x % 5 == 0, range(1, 1000))))

if __name__ == '__main__':
    main()
