from __future__ import print_function

def main():
    mx = None
    for a in range(1, 100):
        for b in range(1, 100):
            mx = max(mx, sum(map(int, str(a**b))))
    print(mx)

if __name__ == '__main__':
    main()
