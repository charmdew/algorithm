import sys

input = sys.stdin.readline

S = input().rstrip()

n = len(S)

# dp[i][j]
# i : 알파벳 소문자 아스키코드값 - 'a' 아스키코드값
# dp[i][j]: 0번째 문자부터 j번째 문자까지 알파벳 등장 횟수 저장
dp = [[0]*n for _ in range(26)]
ord_a = ord('a')

for x in range(n):
    dp[ord(S[x])-ord_a][x] = 1
for i in range(26):
    for j in range(1, n):
        dp[i][j] += dp[i][j-1]

for _ in range(int(input())):
    a, l, r = input().split()
    r = int(r)
    l = int(l)

    if l == 0:
        print(dp[ord(a)-ord_a][r])
    else:
        print(dp[ord(a)-ord_a][r]-dp[ord(a)-ord_a][l-1])