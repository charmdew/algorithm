import sys

input = sys.stdin.readline

N, K = map(int, input().split())

country = [[] for _ in range(N)]
for i in range(N):
    country[i] = list(map(int, input().split()))

# 금, 은, 동 순으로 정렬
country.sort(key=lambda x: [-x[1], -x[2], -x[3]])

# 메달 수 별 등수 저장
rank = {}

# 국가 K의 등수 저장
answer = 0

for i, c in enumerate(country):
    x = 'G'+str(c[1])+'S'+str(c[2])+'B'+str(c[3])
    if x not in rank:
        rank[x] = i+1

    if c[0] == K:
        answer = rank[x]
        break
        
print(answer)