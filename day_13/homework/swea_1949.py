# 등산로 조성
# D4

from pprint import pprint
import sys


def is_lowest(pos):
    cr = pos[0]
    cc = pos[1]
    for dr, dc in directions:
        nr = cr + dr
        nc = cc + dc
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            continue
        # 이동 가능한 좌표가 없는 경우 -> 4방향 좌표의 높이가 같거나 높은 경우
        if grid[nr][nc] <= grid[cr][cc]:
            return False
    return True


def dfs(curr_pos, distance):
    global grid
    global visited
    global max_distance

    cr = curr_pos[0]
    cc = curr_pos[1]
    n = len(grid)

    if is_lowest(curr_pos):
        max_distance = max(max_distance, distance)
        return

    for dr, dc in directions:
        nr = cr + dr
        nc = cc + dc
        # 좌표 유효성 검사
        if nr < 0 or nr >= n or nc < 0 or nc >= n:
            continue
        if visited[nr][nc]:
            continue
        # 현재 좌표의 높이와 같거나 높은 곳으로는 가지 못함
        if grid[nr][nc] >= grid[cr][cc]:
            continue
        # 다음 좌표 방문 처리
        visited[nr][nc] = True
        # print(f"visit {(nr, nc)}")
        # dfs
        dfs((nr, nc), distance+1)
        # 다음 좌표 방문 원복
        visited[nr][nc] = False


def main(test_case):
    global grid
    global visited
    global N

    N, K = map(int, input().split())

    max_height = 0
    max_height_position = []

    for r in range(N):
        row = list(map(int, input().split()))
        for c, v in enumerate(row):
            if max_height <= v:
                max_height = v
                max_height_position.append((r, c))
        grid.append(row)

    visited = [[False for _ in range(N)] for _ in range(N)]
    for max_pos in max_height_position:
        # print(f"start_pos: {max_pos}")
        init_distance = 1
        dfs(max_pos, init_distance)
    print(max_distance)


if __name__ == "__main__":
    sys.stdin = open('../inputs/input_1949.txt')

    T = int(input())
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    grid = []
    visited = []
    max_distance = 0
    N = 0
    for tc in range(1, T+1):
        main(tc)
        break
