import sys

n, k = map(int, input().split())

dp = [1e9] * (100001)

for _ in range(n):
    coin = int(input())

    if dp[coin] == 1:
        continue
    
    dp[coin] = 1

    for x in range(coin+1, k+1):
        if dp[x-coin] + 1 < dp[x]:
            dp[x] = dp[x-coin] + 1

print(dp[k] if dp[k] < 1e9 else -1)