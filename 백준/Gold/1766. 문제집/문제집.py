import heapq
import sys

input = sys.stdin.readline

N, M = map(int, input().split())

# 진입차수 저장
indegree = [0]*(N+1)
graph = [[] for _ in range(N+1)]

# '먼저 푸는 것이 좋은 문제'에 대한 정보 저장
for _ in range(M):
    A, B = map(int, input().split())
    indegree[B] += 1
    graph[A].append(B)

# 가능한 쉬운 문제부터 풀어야 함
# 1번..N번 문제는 난이도 순 => 최소힙 사용
pq = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

result = []
while pq:
    now = heapq.heappop(pq)
    result.append(now)

    for x in graph[now]:
        indegree[x] -= 1

        if indegree[x] == 0:
            heapq.heappush(pq, x)

print(*result)