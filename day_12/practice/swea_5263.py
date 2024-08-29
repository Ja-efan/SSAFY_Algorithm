# 12d_practice
# 그래프 최소 비용 (D4)
# 모든 vertex에 대해서 최단 경로를 탐색 -> 플로이드 워셜

from pprint import pprint
def main():
    INF = float('inf')
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        adj_matrix = [list(map(int, input().split())) for _ in range(N)]

        # print(adj_list)

        # 인접 행렬 초기화
        # r != c 이면서 a_ij 가 0인 경우 즉, 인접하지 않은 경우 INF 할당
        for r in range(N):
            for c in range(N):
                if r == c: continue
                if adj_matrix[r][c] == 0:
                    adj_matrix[r][c] = INF

        # 모든 정점을 경유 정점(k)으로 지정
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if adj_matrix[i][j] > adj_matrix[i][k] + adj_matrix[k][j]:
                        adj_matrix[i][j] = adj_matrix[i][k] + adj_matrix[k][j]

        # 최단 경로 중 가장 큰 값
        max_shortest = 0

        for r in range(N):
            for c in range(N):
                if max_shortest < adj_matrix[r][c]:
                    max_shortest = adj_matrix[r][c]

        print(f"#{tc} {max_shortest}")

if __name__ == "__main__":
    # import sys
    # sys.stdin = open("../inputs/input_5263.txt")
    main()