from collections import deque

structures = {
    1 : [[-1, 0], [1, 0], [0, -1], [0, 1]],  # 상 하 좌 우
    2 : [[-1, 0],[1, 0]],  # 상 하
    3 : [[0, -1],[0, 1]],  # 좌우
    4 : [[-1, 0],[0, 1]],  # 상 우
    5 : [[1, 0],[0, 1]],  # 하 우
    6 : [[1, 0],[0, -1]],  # 하 좌
    7 : [[-1, 0],[0, -1]],  # 상 좌
}

T = int(input())  # 총 테스트케이스 개수
for tc in range(1, T+1):
    N, M, R, C, L = map(int, (input().split()))
    """
    N : 지하 터널 세로 크기 
    M : 지하 터널 가로 크기 
    R : 맨홀 뚜껑 y좌표 
    C : 맨홀 뚜껑 x좌표 
    L : 탈출 후 소요된 시간 
    """

    tunnel = []
    for _ in range(N):
        tunnel.append(list(map(int, input().split())))

    # '방문 체크 리스트' 이자 '도달 시간 체크 리스트'
    visited = [[0 for _ in range(M)] for _ in range(N)]

    # 맨홀 뚜껑 좌표 enqueue
    queue = deque([[R,C]])

    # 시작 지점은 1시간 지정 (맨홀 뚜껑 좌표)
    visited[R][C] = 1
    cnt = 0  # 방문 가능한 터널 좌표 개수
    while queue:
        y,x = queue.popleft()

        structure = structures[tunnel[y][x]]

        if visited[y][x] > L :  # 탈출 후 주어진 시간이 초과된 경우 테스트 케이스 종료
            break

        cnt += 1  # 방문 가능 지점 + 1
        for dir in structure:
            ny = y + dir[0]
            nx = x + dir[1]

            # 좌표 유효성 검사
            if 0 > ny or ny >= N or 0 > nx or nx >= M:
                continue

            # 터널이 없는 장소 검사
            if tunnel[ny][nx] == 0:
                continue

            # 방문 여부 검사
            if visited[ny][nx]:
                continue

            connected = False  # 다음 좌표 (ny, nx)와의 연결 여부 확인
            for next_dir in structures[tunnel[ny][nx]]:
                if (ny + next_dir[0]) == y and (nx + next_dir[1]) == x:
                    connected = True  # 연결 가능한 경우
                    break

            # tunnel[y][x]와 tunnel[ny][nx]의 연결 여부 검사
            if not connected :
                continue

            # 해당 지점까지 소요 시간 업데이트
            visited[ny][nx] = visited[y][x] + 1

            # 큐에 좌표 추가
            queue.append([ny, nx])

    print(f"#{tc} {cnt}")
