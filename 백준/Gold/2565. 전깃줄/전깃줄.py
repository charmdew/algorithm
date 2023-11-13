import sys 

n = int(input())

# 전깃줄들이 전봇대에 연결되는 위치 정보
lines = [1e9] * 501
for _ in range(n):
    idx, to = map(int, input().split())
    lines[idx] = to

# cnt[i] : i번째 위치까지 증가하는 수열 최대 원소 개수
cnt = [0] * (501)

for x in range(1, 501):
    for i in range(1, x):
        if lines[i] < lines[x]:
            cnt[x] = max(cnt[x], cnt[i]+1)

print(n-max(cnt))