from collections import deque

T = int(input())  # 총 테스트 케이스 개수

for tc in range(1, T+1):
    N = int(input())  # 지도의 크기 (NxN)

    grid = []
    for _ in range(N):
        grid.append(list(map(int, list(input()))))

    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    src = [0, 0]
    queue = deque([src])
    INF = float('inf')
    recover_time = [[INF for _ in range(N)] for _ in range(N)]
    recover_time[0][0] = 0  # 시작점의 복구 시간은 0

    while queue:
        y, x = queue.popleft()

        for dir in directions:
            ny = y + dir[0]
            nx = x + dir[1]

            # 범위 체크
            if 0 > ny or ny >= N or 0 > nx or nx >= N:
                continue

            # 새로 계산한 복구 시간
            new_recover_time = recover_time[y][x] + grid[ny][nx]

            # 더 짧은 복구 시간이 발견되었을 때만 업데이트
            if new_recover_time < recover_time[ny][nx]:
                recover_time[ny][nx] = new_recover_time
                queue.append([ny, nx])

    print(f"#{tc} {recover_time[-1][-1]}")