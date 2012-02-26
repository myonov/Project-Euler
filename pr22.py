from __future__ import print_function

def main():
    names = sorted(open('names.txt').read().replace('"', '').split(','))
    a = 0
    for i, name in enumerate(names):
        s = 0
        for x in name:
            s += ord(x) - ord('A') + 1
        a += (i + 1) * s
    print(a)

if __name__ == '__main__':
    main()
