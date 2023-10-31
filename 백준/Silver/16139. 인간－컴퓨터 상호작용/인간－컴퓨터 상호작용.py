import sys

input = sys.stdin.readline

S = input().rstrip()

n = len(S)

# dp[i][j]
# j : 알파벳 소문자 아스키코드값 - 'a' 아스키코드값
# dp[i][j]: 0번째 문자부터 i번째 문자까지 알파벳 등장 횟수 저장
dp = [[0]*26]
ord_a = ord('a')
dp[0][ord(S[0])-ord_a] = 1

for x in range(1, n):
    dp.append(dp[-1][:])
    dp[x][ord(S[x])-ord_a] += 1

for _ in range(int(input())):
    a, l, r = input().split()
    idx = ord(a)-ord_a
    r = int(r)
    l = int(l)

    if l == 0:
        print(dp[r][idx])
    else:
        print(dp[r][idx]-dp[l-1][idx])