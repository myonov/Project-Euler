from __future__ import print_function

import math

def main():
    l = [map(int, l.strip().split(',')) for l in open('base_exp.txt', 'r')]
    print(max(enumerate(l), key=lambda x: math.log(x[1][0]) * x[1][1])[0]+1)

if __name__ == '__main__':
    main()
