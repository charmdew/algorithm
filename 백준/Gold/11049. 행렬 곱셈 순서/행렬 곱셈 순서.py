# 2차원 DP 사용해야함
# dp[i][j] : i행렬부터 j행렬까지 행렬 곱의 최소값
# PyPy3으로 제출

import sys

input = sys.stdin.readline

N = int(input())

matrix = [list(map(int, input().split())) for _ in range(N)]

dp = [[2 ** 31]*N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for i in range(1, N+1):
    for j in range(0, N-i):
        # 1칸 차이가 나는 행렬곱
        if i == 1:
            dp[j][j+1] = matrix[j][0]*matrix[j][1]*matrix[j+1][1]
            continue

        # 2칸 이상 떨어진 행렬들의 곱의 최솟값
        # ABC 연속행렬 곱의 최솟값 =
        #   min(ABC,
        #       min(A)+min(BC)+마지막행렬곱셈,
        #       min(AB)+min(C)+마지막행렬곱셈
        #      )
        for k in range(j, j+i):
            dp[j][j+i] = min(dp[j][j+i], dp[j][k]+dp[k+1][j+i] + (matrix[j]
                             [0]*matrix[k][1]*matrix[j+i][1]))

print(dp[0][-1])