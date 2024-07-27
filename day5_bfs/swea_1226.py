# [S/W 문제해결 기본] 7일차 - 미로1
from collections import deque
from pprint import pprint
# import sys
# sys.stdin = open("input_1226.txt")

def solution():
    T = 10  # 테스트 케이스 개수 :  10으로 변경 후 제출
    N = 16  # 미로 크기 (NxN)


    for _ in range(T):
        break_point = False
        tc = int(input())
        maze = []
        for _ in range(N):
            maze.append(list(map(int, list(input()))))

        src = 2
        dst = 3
        src_index = []
        dst_index = []
        # 방문 여부 체크 리스트
        visited = [[False for _ in range(N)] for _ in range(N)]

        # 이동 가능 방향 : 하 우 상 좌
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        # 출발점 인덱스 찾기
        for i in range(N):
            for j in range(N):
                if maze[i][j] == src:
                    src_index = [i, j]

        # print(src_index)

        # 큐 선언
        queue = deque([src_index])

        # 출발점 방문 처리
        visited[src_index[0]][src_index[1]] = True

        while queue:
            y, x = queue.popleft()
            # print(y,x)
            for dir in directions:
                ny = y + dir[0]
                nx = x + dir[1]

                # 범위 확인
                if 0 > ny or ny >= N or 0 > nx or nx >= N :
                    continue

                # 벽인지 길인지 확인
                if maze[ny][nx] == 1 :
                    continue

                # 방문했는지 확인
                if visited[ny][nx]:
                    continue

                queue.append([ny, nx])
                visited[ny][nx] = True

                # 종료 조건
                if maze[ny][nx] == dst:
                    print(f"#{tc} 1")
                    # return
                    break_point = True  # 해당 테스트 케이스 종료
                    break

        if break_point:  # 해당 테스트 케이스 종료
            continue

        # while 문 종료 -> 도착점 도달 불가
        print(f"#{tc} 0")
        # return

solution()