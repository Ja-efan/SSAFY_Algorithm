from collections import deque

def bfs(road, src):
    N = len(road)
    M = len(road[0])
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    queue = deque(src)
    visited[src[0]][src[1]] += 1

    while deque:
        curr = queue.popleft()
        # visited[curr] += 1
        curr_y = curr[0]
        curr_x = curr[1]

        for dir in directions:
            dy = curr_y + dir[0]
            dx = curr_x + dir[1]
            if dy < 0 or dy >= N or dx < 0 or dx >= M or road[dy][dx] == 0:
                # road의 범위를 벗어나거나 장애물이 존재하는 경우
                continue
            elif visited[dy][dx] == -1:
                # [dy, dx]를 방문하지 않은 경우
                visited[dy][dx] = visited[curr_y][curr_x] + 1
                queue.append([dy,dx])
            else:
                # [dy, dx]를 이미 방문한 경우
                # 거리가 더 긴 경우
                if visited[dy][dx] <= visited[curr_y][curr_x] + 1:
                    continue
                else :
                    visited[dy][dx] = visited[curr_y][curr_x] + 1
                    queue.append([dy, dx])


road = [[1,0,1,1,1,1],[1,0,1,0,1,0],[1,0,1,0,1,1],[1,1,1,0,1,1]]
bfs(road, [0,0])