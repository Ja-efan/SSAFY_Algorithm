# day_9 homewok
# 파핑파핑 지뢰찾기

from collections import deque

def main():
    T = int(input())
    directions = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
    for tc in range(1, T+1):
        N = int(input())
        grid = [list(input().rstrip()) for _ in range(N)]
        visited = [[False for _ in range(N)] for _ in range(N)]
        for r in range(N):
            for c in range(N):
                bomb_cnt = 0
                # 지뢰가 없는 칸을 돌면서 주변 8방향에 지뢰가 몇 개 있는지 확인한다.
                if grid[r][c] == '*': continue  # 지뢰인 경우 skip
                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc
                    # 범위 확인
                    if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                    # 지뢰인 경우 지뢰 개수 추가
                    if grid[nr][nc] == "*":
                        bomb_cnt += 1
                # 현재 좌표 값을 주변 폭탄 개수로 변경
                grid[r][c] = bomb_cnt

        # 현재 상황 : 모든 좌표의 값이 8방면 폭탄 개수 혹은 폭탄
        # -> 주변에 폭탄이 없는 좌표(r,c)를 골라서 연쇄적으로 폭탄을 터트린다.
        click_cnt = 0
        for r in range(N):
            for c in range(N):
                # 주변에 폭탄이 있거나, 폭탄이 위치한 좌표인 경우
                if grid[r][c] != 0: continue
                if visited[r][c]: continue
                # 좌표 값이 0인 부분들의 연쇄적인 상호작용이 발생 -> bfs
                queue = deque([(r, c)])
                visited[r][c] = True
                while queue:
                    curr_r, curr_c = queue.popleft()
                    for dr, dc in directions:
                        nr, nc = curr_r + dr, curr_c + dc
                        # 좌표 유효성 검사
                        if nr < 0 or nr >= N or nc < 0 or nc >= N: continue
                        if grid[nr][nc] == "*": continue
                        if visited[nr][nc]: continue

                        visited[nr][nc] = True
                        if grid[nr][nc] != 0: continue
                        queue.append((nr, nc))
                click_cnt += 1

        # 0으로 연쇄적으로 터트려진 좌표 외에 하나하나 클릭해야 할 좌표들
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 0: continue
                if grid[r][c] == "*": continue
                if visited[r][c]: continue
                click_cnt += 1
        print(f"#{tc} {click_cnt}")


if __name__ == "__main__":
    main()