# 10d_practice
# 하나로
# D4

from itertools import combinations


class DisjointSet:
    def __init__(self, number_of_items):
        self.head = [0 for _ in range(number_of_items + 1)]
        self.rank = [0 for _ in range(number_of_items + 1)]
        self.n = number_of_items

    def make_set(self, item):
        self.head[item] = item

    def make_set_all(self):
        for item in range(1, self.n + 1):
            self.make_set(item)

    def find_head(self, item):
        if self.head[item] != item:
            self.head[item] = self.find_head(self.head[item])
        return self.head[item]

    def find_head_all(self):
        n = len(self.head)
        for item in range(1, n + 1):
            self.find_head(item)

    def union(self, item1, item2):
        h1 = self.find_head(item1)
        h2 = self.find_head(item2)

        if h1 != h2:
            if self.rank[h1] > self.rank[h2]:
                self.head[h2] = h1
            elif self.rank[h1] < self.rank[h2]:
                self.head[h1] = h2
            else:
                self.head[h2] = h1
                self.rank[h1] += 1


def kruskal_mst(vertices, edges):
    n = len(vertices)
    edges.sort(key=lambda x: x[2])  # 환경 부담금 기준 정렬 (오름차순)
    ds = DisjointSet(n)
    ds.make_set_all()

    mst_cost = 0
    mst_edges = 0
    mst_edge_list = []
    for edge in edges:
        v = edge[0]
        u = edge[1]
        w = edge[2]
        if ds.find_head(v) != ds.find_head(u):
            ds.union(v, u)
            mst_edges += 1
            mst_cost += w
            mst_edge_list.append(edge)
    return mst_cost


def cal_env_fee(island_1, island_2, e):
    x1, y1 = island_1
    x2, y2 = island_2
    L = ((x1 - x2) ** 2 + (y1 - y2) ** 2)
    fee = e * L
    return fee


def main():
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())  # 섬의 개수
        x_list = list(map(int, input().split()))
        y_list = list(map(int, input().split()))
        E = float(input())

        island_pos_list = []
        for x, y in zip(x_list, y_list):
            island_pos_list.append((x, y))

        island_comb = list(combinations(list(range(1, N + 1)), 2))
        tunnels = []
        for comb in island_comb:
            island_1 = island_pos_list[comb[0] - 1]
            island_2 = island_pos_list[comb[1] - 1]
            env_fee = cal_env_fee(island_1=island_1, island_2=island_2, e=E)
            tunnels.append((comb[0], comb[1], env_fee))

        cost = round(kruskal_mst(vertices=list(range(1, N + 1)), edges=tunnels))
        print(f"#{tc} {cost}")


if __name__ == "__main__":
    import sys

    sys.stdin = open("../inputs/input_1251.txt")
    main()
