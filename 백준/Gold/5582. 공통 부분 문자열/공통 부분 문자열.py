# dp 활용
# dp[i][j] : str1의 1부터 i까지의 글자와 str2의 1부터 j까지의 글자 사이의 공통 부분 문자열 길이

import sys

input = sys.stdin.readline

str1 = input().rstrip()
str2 = input().rstrip()

N = len(str1)
M = len(str2)

dp = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        # 같은 문자인 경우 dp값 1로 설정
        if str1[i] == str2[j]:
            dp[i][j] = 1

for i in range(1, N):
    for j in range(1, M):
        # 이전 문자와 현재 문자 모두 같다면
        if str1[i-1] == str2[j-1] and str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + 1

result = 0
# dp에서 최댓값 구하기
for i in range(N):
    for j in range(M):
        result = max(result, dp[i][j])

print(result)