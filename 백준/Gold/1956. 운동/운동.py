import sys 

input = sys.stdin.readline 

INF = int(1e9)

# 노드의 개수 및 간선의 개수를 입력받기
V, E = map(int, input().split())

# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (V + 1) for _ in range(V + 1)]

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(E):
    # a에서 b로 가는 거리는 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, V + 1):
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

result = INF
# 도로의 길이의 합이 가장 작은 사이클을 찾기
for x in range(1, V + 1):
    result = min(result, graph[x][x])

# 운동 경로를 찾는 것이 불가능한 경우에는 -1
print(-1 if result == INF else result)