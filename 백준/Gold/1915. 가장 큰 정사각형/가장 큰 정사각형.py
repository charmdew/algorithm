# dp 활용!!
# - [i-1][j-1] 칸과 [i-1][j]칸과 [i][j-1]칸중 가장 최소인 것의 +1이
#   해당 칸이 정사각형 오른쪽 아래 꼭짓점일 때 최대 크기의 정사각형임

import sys

input = sys.stdin.readline

n, m = map(int, input().split())

arr = [list(map(int, list(input().rstrip()))) for _ in range(n)]

dp = [[0]*m for _ in range(n)]

result = 0
# 가능한 정사각형 구하기
for r in range(0, n):
    for c in range(0, m):
        if r == 0 or c == 0:
            dp[r][c] = arr[r][c]

        elif arr[r][c] == 0:
            dp[r][c] = 0

        else:
            dp[r][c] = min(dp[r-1][c-1], dp[r-1][c], dp[r][c-1]) + 1

        result = max(dp[r][c], result)

print(result*result)