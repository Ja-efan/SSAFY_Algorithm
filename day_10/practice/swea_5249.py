# 10d_practice
# 최소 신장 트리
# prim algorithm

from collections import defaultdict
import heapq
import sys


def prim():
    T = int(input())  # 테스트 케이스 개수
    for tc in range(1, T+1):
        V, E = map(int, input().split())
        visited = set()
        adj_dict = defaultdict(list)
        mst_weight = 0
        for _ in range(E):
            s_v, e_v, weight = map(int, input().split())  # start-vertex, end-vertex, weight
            adj_dict[s_v].append((e_v, weight))
            adj_dict[e_v].append((s_v, weight))

        init_vertex = min(list(adj_dict.keys()))  # 초기 정점
        min_heap = [(weight, init_vertex, e_v) for e_v, weight in adj_dict[init_vertex]]  # 초기 정점에 연결된 엣지

        visited.add(init_vertex)  # 초기 정점 방문 처리 

        heapq.heapify(min_heap)  # 힙 변환 
        while min_heap: 
            weight, curr_v, adj_v = heapq.heappop(min_heap)  
            if adj_v in visited:  # 방문한 정점인 경우 
                continue

            visited.add(adj_v)  # 인접 정점 방문 처리 
            mst_weight += weight  # 가중치 추가 

            for e_v, weight in adj_dict[adj_v]:  # 인접 정점의 인접 정점 확인 
                if e_v in visited:  # 방문한 경우 스킵 
                    continue
                heapq.heappush(min_heap, (weight, adj_v, e_v))  # 힙 추가 

        print(f"#{tc} {mst_weight}")


if __name__ == "__main__":
    sys.stdin = open("./inputs/input_5249.txt")
    prim()
