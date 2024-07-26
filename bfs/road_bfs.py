import sys
from collections import deque

sys.stdin = open("practice_input.txt")

def get_road_move_time(road, n, m):
    # 4 방향 탐색을 해야한다.
    # 하 우 상 좌
    # dxy 를 for loop로 돌면서 현재 좌표에서 dx, dy를 더해주면, 상하좌우로 이동할 수 있다.
    dxy = [[1, 0],[0, 1],[-1, 0],[0, -1]]

    # BFS는 큐로 구현 -> deque
    # 문제에서는 [1,1] => [n,m]
    # 입력값을 [0,0] => [n-1, m-1]
    queue = deque([(0, 0)])

    # 공간 복사하고, 각 좌표까지 걸리는 최단 이동거리를 저장
    # 노드에 방문한 적 있는 지 확인하는 용도
    # 해당 좌표까지 이동 거리 계산 용도
    # 꼭 -1로 초기화 하지 않아도 됨. 자유롭게 자신만의 방법으로 초기화
    distance = [[-1 for _ in range(m)] for _ in range(n)]
    distance[0][0] = 0  # 처음 시작 부분은 0으로 하기로 문제가 정함

    while queue:  # 큐가 빌 때까지 원소를 꺼내고 방문하는 행위를 반복
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy  # 현재 위치에서 각 방향으로 이동

            # [nx, ny]가 갈 수 있는 곳인지를 체크
            # 1. 도로 범위 안에 포함될 것
            # 2. 방문한 적이 없을 것 (내가 갈 곳이 -1 이어야 함)
            # 3. 갈 수 있는 곳 일것 (길이어야 한다. (1) 이어야 함)
            if 0 <= nx < n and 0 <= ny < m and distance[nx][ny] == -1 and road[nx][ny] == 1:
                queue.append((nx, ny))

                # 현재 위치까지 오는데 걸린 이동 횟수 + 1 값을
                # 다음에 이동해야 할 좌표에 입력을 한다
                distance[nx][ny] = distance[x][y] + 1

                if nx == n-1 and ny == m-1 :
                    return distance[nx][ny]

        # while 문을 빠져나왔다는 소리는, 결국 목적지에 도착하지 못했다
        # 문제에서 요구하는 사항을 반환하면 됨
        return -1

n, m = map(int, input.split())
road = [list(map(int, input())) for _ in range(n)]


