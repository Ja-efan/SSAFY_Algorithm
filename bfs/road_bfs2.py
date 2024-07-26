import sys
from collections import deque

sys.stdin = open("practice_input.txt")

# 기존에는 큐에 다음에 방문할 좌표를 집어 넣음
# 이번에는 방문할 좌표 + 여태까지 이동한 횟수를 같이 큐에 넣어 줌
# 이렇게 풀어도 방문 여부를 확인하는 변수는 있어야 함
# 문제에서 큐에 좌표를 집어넣을 때, 부가 데이터를 넣어달라고 하는 문제들이 있음


def get_road_move_time(road, n, m):

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    # 방문 여부만 확인
    visited = [[False for _ in range(m)] for _ in range(n)]

    # 시작 좌표 + 현재 까지 이동 거리
    queue = deque([0,0,0])

    while queue:
        x, y, dist = queue.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            next_dist = dist + 1
