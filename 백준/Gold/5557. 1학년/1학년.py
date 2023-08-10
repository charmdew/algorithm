"""
dfs를 사용해 문제를 푸는 경우 2^n의 시간복잡도가 되므로 시간초과

DP를 활용해야함!
- DP[i][j] : i번째까지, j가 되는 경우의 수
- 초기값 
    DP[0][nums[0]] = 1
- 점화식  
    DP[i][j+nums[i]] += DP[i-1][j]
    DP[i][j-nums[i]] += DP[i-1][j]
"""

import sys

input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [[0]*(21) for _ in range(N)]
# 초기값 설정
dp[0][nums[0]] = 1

for i in range(1, N-1):
    for j in range(21):
        if j + nums[i] <= 20:
            dp[i][j+nums[i]] += dp[i-1][j]
        if j - nums[i] >= 0:
            dp[i][j-nums[i]] += dp[i-1][j]
print(dp[N-2][nums[-1]])