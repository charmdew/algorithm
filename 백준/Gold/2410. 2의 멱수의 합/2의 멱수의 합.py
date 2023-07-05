# 어떤 자연수 N을 2의 멱수의 합으로 나타내는 경우의 수

"""
N = 1 -> 1
N = 2 -> 1+1, 2
N = 3 -> 1+1+1, 2+1
N = 4 -> 1+1+1+1, 2+1+1, 2+2, 4
N = 5 -> 1+1+1+1+1, 2+1+1+1, 2+2+1, 4+1

N이 홀수인 경우 -> (N-1일 때 경우+ 1) : dp[N-1]
N이 짝수인 경우 -> (N-1일 때 경우+ 1) + (N/2일 때 경우 * 2) : dp[N-1]+dp[N//2]
"""

import sys

input = sys.stdin.readline

N = int(input())

dp = [0]*(N+1)
dp[1] = 1

for i in range(2, N+1):
    # 홀수인 경우
    if i % 2 == 1:
        dp[i] = dp[i-1]
    # 짝수인 경우
    else:
        dp[i] = dp[i-1]+dp[i//2]
print(dp[N] % 1000000000)