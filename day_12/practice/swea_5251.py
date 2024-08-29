# 12d_practice
# 최소 이동 거리 (D4)
# 최단 경로 - Dijkstra

import heapq

def main():
    INF = float('inf')

    T = int(input())
    for tc in range(1, T+1):
        N, E = map(int, input().split()) # N: 연결 지점 번호, E: 도로의 개수

        adj_matrix = [[0 for _ in range(N+1)] for _ in range(N+1)]
        # print(adj_matrix)
        for _ in range(E):
            s, e, w = map(int, input().split())
            adj_matrix[s][e] = w

        # vertex 0에서 각 vertex로의 거리를 저장할 리스트
        distances = [INF for _ in range(N+1)]
        # 시작 정점의 거리는 0으로 설정
        distances[0] = 0
        # 시작 정점과 거리를 우선순위 큐에 삽입
        heap = [] # (w_i, v_i)
        heapq.heapify(heap)
        heapq.heappush(heap, (0, 0))
        while heap:
            # 가장 짧은 거리를 가지는 정점 추출
            w, v = heapq.heappop(heap)
            if distances[v] < w: continue
            # 추출한 정점과 인접한 정점을 모두 확인
            for u, connected in enumerate(adj_matrix[v]):
                # print(adj_matrix[v])
                if not connected: continue
                if distances[u] > distances[v] + adj_matrix[v][u]:
                    distances[u] = distances[v] + adj_matrix[v][u]
                    heapq.heappush(heap, (distances[u], u))

        print(f"#{tc} {distances[-1]}")



if __name__ == "__main__":
    import sys
    sys.stdin = open("../inputs/input_5251.txt")
    main()