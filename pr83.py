from __future__ import print_function

import heapq

class Node(object):
    def __init__(self, neighbours=None):
        self.g = neighbours or []

class Edge(object):
    def __init__(self, to, dist):
        self.to = to
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist

    def __eq__(self, other):
        return self.dist == other.dist and\
               self.to == other.to


def main():
    m = [
        map(int, line.strip().split(','))
        for line in open('matrix.txt')
    ]

    deltaxy = [
        (-1, 0), (0, 1), (1, 0), (0, -1)
    ]

    l = len(m) # 80x80
    g = [
        [Node() for i in range(l)] for i in range(l)
    ]

    for i in range(l):
        for j in range(l):
            for dx, dy in deltaxy:
                di = i + dx
                dj = j + dy

                if di < 0 or di >= l or dj < 0 or dj >= l:
                    continue

                g[i][j].g.append(Edge(g[di][dj], m[di][dj]))

    #dijkstra algorithm
    start = g[0][0]
    end = g[-1][-1]

    d = {start: m[0][0]}
    q = []
    for e in g[0][0].g:
        heapq.heappush(q, Edge(e.to, d[start] + e.dist))

    while True:
        e = None
        while q:
            e = heapq.heappop(q)
            if e.to not in d:
                break

        if not e or e.to in d:
            break

        d[e.to] = e.dist
        for e1 in e.to.g:
            heapq.heappush(q, Edge(e1.to, e1.dist + d[e.to]))

    print(d[end])


if __name__ == '__main__':
    main()
