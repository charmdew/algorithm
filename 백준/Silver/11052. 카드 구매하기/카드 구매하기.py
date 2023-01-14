import sys

input = sys.stdin.readline

# 민규가 구매하려고 하는 카드의 개수 N
N = int(input())

# P[i] : 카드가 i개 포함된 카드팩의 가격
P = [0]+[*map(int, input().split())]

# dp[i] : 카드 i개를 갖기 위해 지불해야 하는 금액 최댓값
dp = [*P]

"""
N   = 1 + N-1
    = 2 + N-2
    ...
    = N//2 + N-(N//2)
"""
for i in range(1, N+1):
    for j in range(1, i//2+1):
        dp[i] = max(dp[j]+dp[i-j], dp[i])

print(dp[N])