def bellman_ford(graph, start):
    v_count = len(graph)  # 그래프의 정점 수

    # 시작 정점에서 모든 정점까지의 거리를 무한대로 초기화
    distances = {v: float('inf') for v in graph}
    distances[start] = 0  # 시작 정점의 거리를 0으로 설정
    # 모든 정점에 대해 (정점 개수 - 1) 반복
    for i in range(v_count - 1):
        updated = False  # 거리 업데이트 여부 확인
        # 각 정점별 인접한 간선을 순회
        for u in graph:
            for v, weight in graph[u].items():
                # [ 시작 정점(u)에 도달하는 최소 거리 + 가중치 ] 가 [ 도착 정점(v)의 최소 거리] 보다 작은 경우 갱신
                if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                    distances[v] = distances[u] + weight  # v의 거리를 갱신합니다.
                    updated = True  # 거리 업데이트 플래그를 참으로 설정

        # 거리 업데이트가 발생하지 않았으면 반복을 조기 종료
        if not updated:
            break

    # 음수 사이클 검출
    for u in graph:
        for v, weight in graph[u].items():
            # 만약 거리 업데이트가 발생하면 음수 사이클이 존재함을 의미
            if distances[u] != float('inf') and distances[u] + weight < distances[v]:
                print("음수 사이클 발생")
                return
    return distances  # 최단 거리 리스트를 반환합니다.

# 예시 그래프
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': 3, 'D': 2, 'E': 3},
    'C': {'B': 1, 'D': 4, 'E': 5},
    'D': {'E': -3},
    'E': {'F': 2},
    'F': {}
}

# 시작 정점 설정
start_vertex = 'A'

# 벨만-포드 알고리즘 실행
result = bellman_ford(graph, start_vertex)

print(f"'{start_vertex}': {result}")
