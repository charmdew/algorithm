import sys 
import heapq

input = sys.stdin.readline 

# N, M, X 입력
N, M, X = map(int, input().split())

# 도로 정보 입력
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))

# 다익스트라 이용
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        t, now = heapq.heappop(q)

        if time[now] < t:
            continue
            
        for x, tt in graph[now]:
            cost = time[now] + tt

            if cost < time[x]:
                time[x] = cost
                heapq.heappush(q, (cost, x))

# 학생들이 오고가는데 걸리는 최단 시간 저장
result = [0] * (N+1)

# 1~N에서 X까지 가는 최단 시간 구하기
for i in range(1, N+1):
    time = [1e9] * (N+1)
    time[i] = 0
    dijkstra(i)
    result[i] = time[X]

# X에서 1~N까지 가는 최단 시간 구하기
time = [1e9] * (N+1)
time[X] = 0
dijkstra(X)
for i in range(1, N+1):
    result[i] += time[i]

# 가장 오래 걸리는 학생의 소요시간
print(max(result))