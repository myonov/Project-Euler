from __future__ import print_function

def main():
    limit = 300000
    s = ''.join((str(i) for i in range(limit)))
    #''.join is much faster than concatenating with +=

    print(reduce(lambda x, y: x*int(y), [s[1], s[10], s[100], s[1000],
          s[10000], s[100000], s[1000000]], 1))

if __name__ == '__main__':
    main()
