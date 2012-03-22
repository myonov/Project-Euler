from __future__ import print_function

def orient(x1, y1, x2, y2, x3, y3):
    return (y3 - y1) * (x2 - x1) - (x3 - x1) * (y2 - y1)

def main():
    a = 0
    for l in open('triangles.txt', 'r'):
        p = map(float, l.strip().split(','))
        b = [orient(p[0], p[1], p[2], p[3], 0, 0),
             orient(p[2], p[3], p[4], p[5], 0, 0),
             orient(p[4], p[5], p[0], p[1], 0, 0)]
        if all(map(lambda x: x < 0, b)) or all(map(lambda x: x > 0, b)):
            a += 1
    print(a)

if __name__ == '__main__':
    main()
