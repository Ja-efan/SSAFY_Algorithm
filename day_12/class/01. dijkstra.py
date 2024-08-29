import heapq, math
def dijkstra(graph, start):
    distances = {v: math.inf for v in graph}  # 모든 정점의 거리를 무한대로 초기화
    distances[start] = 0  # 시작 정점의 거리를 0으로 설정
    min_heap = []
    heapq.heappush(min_heap, [0, start])  # 시작 정점을 힙에 추가
    
    # 우선순위 큐에 아무것도 들어있지 않을 때까지 최단거리 갱신 반복 
    while min_heap:
        # 현재 정점과 해당 정점까지 도달하는 데 걸리는 거리
        current_distance, current_vertex = heapq.heappop(min_heap)
        
        # 정점까지의 기존 거리보다 갱신된 거리가 크다면 그냥 넘어감
        if distances[current_vertex] < current_distance: continue
        
        # 인접한 노드에 대해서 갱신된 거리가 기존 거리보다 작다면 갱신하고, 우선순위 큐에 삽입 
        for adjacent, weight in graph[current_vertex].items():
            distance = current_distance + weight  # 현재 정점까지의 거리 + 인접 정점까지의 거리
            if distance < distances[adjacent]:  # 새로운 거리가 더 짧으면 갱신
                distances[adjacent] = distance
                heapq.heappush(min_heap, [distance, adjacent])  # 우선순위 큐에 추가

    return distances

graph = {
    'a': {'b': 3, 'c': 5},
    'b': {'c': 2},
    'c': {'b': 1, 'd': 4, 'e': 6},
    'd': {'e': 2, 'f': 3},
    'e': {'f': 6},
    'f': {}
}
start_v = 'a'
res = dijkstra(graph, start_v)
print(res)  # {'a': 0, 'b': 3, 'c': 5, 'd': 9, 'e': 11, 'f': 12}
