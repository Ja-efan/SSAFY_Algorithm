# day_10 homework
# 그룹 나누기
# Disjoint Set

import sys


class DisjointSet:
    def __init__(self, N):
        self.parent = [0 for _ in range(N + 1)]
        self.rank = [0 for _ in range(N + 1)]

    def init_parent(self, x):
        self.parent[x] = x

    def find_representative(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find_representative(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find_representative(x)
        ry = self.find_representative(y)

        if rx != ry:
            if self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            elif self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1


def disjoint_set():
    T = int(input())

    for tc in range(1, T + 1):
        N, M = map(int, input().split())
        pairs = list(map(int, input().split()))

        ds = DisjointSet(N)
        for i in range(1, N + 1):
            ds.init_parent(i)

        for i in range(0, 2 * M - 1, 2):
            x_r = ds.find_representative(pairs[i])
            y_r = ds.find_representative(pairs[i + 1])
            if x_r != y_r:
                ds.union(x_r, y_r)

        for i in range(1, N + 1):
            ds.find_representative(i)
        # print(set(ds.parent))
        print(f"#{tc} {len(set(ds.parent)) - 1}")


if __name__ == "__main__":
    sys.stdin = open('../inputs/input_5248.txt')
    disjoint_set()
