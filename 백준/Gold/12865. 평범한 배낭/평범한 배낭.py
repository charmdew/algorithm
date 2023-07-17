import sys 

input = sys.stdin.readline 

N, K = map(int, input().split())

goods = []
dp = [0] * (K+1)
for _ in range(N):
    W, V = map(int, input().split())

    goods.append((W, V))

for w, v in goods:
    for i in range(K, w-1, -1):
        dp[i] = max(dp[i-w]+v, dp[i])

print(dp[K])