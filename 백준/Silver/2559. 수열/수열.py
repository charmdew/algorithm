import sys

input = sys.stdin.readline

N, K = map(int, input().split())

degree = list(map(int, input().split()))

# 누적합 구하기
for i in range(1, N):
    degree[i] += degree[i-1]

result = degree[K-1]

for i in range(K, N):
    result = max(result, degree[i]-degree[i-K])

print(result)