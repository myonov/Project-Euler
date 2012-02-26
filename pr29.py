from __future__ import print_function

def main():
    s = set()
    for i in range(2, 101):
        for j in range(2, 101):
            s.add(i ** j)
    print(len(s))

if __name__ == '__main__':
    main()
