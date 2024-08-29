INF = float('inf')  # 무한대

def floyd_warshall(graph):
    V = len(graph)
    dist = [[INF] * V for _ in range(V)]  # 모든 정점에 대해서 무한대로 초기화
    
    # 자기 자신으로의 거리는 0으로 초기화
    for i in range(V):
        dist[i][i] = 0
    
    # 초기 주어진 가중치에 따라 최초 거리 업데이트
    for u in range(V):
        for v in range(V):
            if graph[u][v] != 0:
                dist[u][v] = graph[u][v]

    for k in range(V):  # 모든 정점을 경유 정점으로 고려
        for i in range(V):  # 시작 정점을 고정 
            for j in range(V):  # 도착 정점을 고정 
                # (시작 정점 -> k 정점) 거리 + ( k 정점 -> 도착 정점) 거리
                # (시작 정점 -> 도착 정점) 거리
                # 경유해서 가는 게 더 가깝다면 갱신
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist  # 최단 경로가 포함된 거리 행렬을 반환 

graph = [
    [0, 4, 2, 5, INF],
    [INF, 0, 1, INF, 4],
    [1, 3, 0, 1, 2],
    [-2, INF, INF, 0, 2],
    [INF, -3, 3, 1, 0]
]

result = floyd_warshall(graph)

# 최단 거리 행렬 출력 
for row in result:
    print(row)
