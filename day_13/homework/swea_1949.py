# 등산로 조성
# D4

from pprint import pprint
#import sys


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
    global grid, visited, max_distance, CONSTRUCT

    cr = curr_pos[0]
    cc = curr_pos[1]
    n = len(grid)

    if is_lowest(curr_pos):
        max_distance = max(max_distance, distance)
        # print(max_distance)
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
        # 원래 가지 못하는 좌표를 깎아내야 더 긴 등산로를 조성할 수 있게 된다.
        # 다음 좌표를 깎아 낼 걸 GLOBAL하게 표시해놓아야 함 -> flag
        # 최대 k 만큼 깎아 낼 수 있고, 모두 깎은 다음에는 원복 시켜야 함
        if grid[nr][nc] >= grid[cr][cc]:
            if not CONSTRUCT:
                tmp_K = K
                CONSTRUCT = True  # 플래그 설정
                # print(f"공사 좌표: {(nr, nc)}")
                while tmp_K:
                    grid[nr][nc] -= 1
                    tmp_K -= 1
                    if grid[nr][nc] >= grid[cr][cc]:
                        continue
                    # 다음 좌표의 높이가 현재 좌표의 높이보다 낮아진 경우 이동 가능
                    visited[nr][nc] = True
                    dfs((nr, nc), distance+1)
                    visited[nr][nc] = False
                grid[nr][nc] += K
                CONSTRUCT = False  # 플래그 원복

            continue

        # 다음 좌표 방문 처리
        visited[nr][nc] = True
        # print(f"visit {(nr, nc)}")

        # dfs
        dfs((nr, nc), distance+1)

        # 다음 좌표 방문 원복
        visited[nr][nc] = False


def main(test_case):
    global grid, visited, N, K

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
    # pprint(grid)

    visited = [[False for _ in range(N)] for _ in range(N)]
    for max_pos in max_height_position:
        visited[max_pos[0]][max_pos[1]] = True
        # print(f"start_pos: {max_pos}")
        init_distance = 1
        dfs(max_pos, init_distance)
        visited[max_pos[0]][max_pos[1]] = False
    print(f"#{test_case} {max_distance}")


if __name__ == "__main__":
    #sys.stdin = open('../inputs/input_1949.txt')

    T = int(input())
    directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    grid, visited = [], []
    N, K, max_distance = 0, 0, 0
    CONSTRUCT = False
    for tc in range(1, T+1):
        main(tc)
        grid, visited = [], []
        N, K, max_distance = 0, 0, 0
