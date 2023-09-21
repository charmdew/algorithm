# N(2 ≤ N ≤ 50), M(1 ≤ M ≤ 13) 입력
N, M = map(int, input().split())

city = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []

for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        elif city[i][j] == 2:
            chicken.append((i, j))

# 치킨집 개수
n_chick = len(chicken)

# 모든 조합 저장하기
case = []

# 조합 구하기
def dfs(comb, i, N, M):
    # M 개수만큼 뽑았으면
    if len(comb) == M:
        case.append(list(comb))
        # print(comb)
        # print(case)
        return

    # 범위를 벗어나면
    if i >= n_chick:
        return

    # i 포함
    comb.append(chicken[i])
    dfs(comb, i+1, N, M)

    # i 포함 안하는 경우
    comb.pop()
    dfs(comb, i+1, N, M)


def distance(ch):
    dist = 0
    # 모든 집에 대해서
    for h in home:
        d = 101
        # 모든 치킨 거리 비교
        for c in ch:
            # print(h[0],h[1], c[0],c[1])
            d = min(abs(c[0]-h[0])+abs(c[1]-h[1]), d)
        dist += d
    return dist


# 치킨집 M개를 뽑는 경우 구하기 (조합)
dfs(list(), 0, N, M)
# print(case)

d_sum = 1300
for c in case:
    d_sum = min(d_sum, distance(c))
print(d_sum)


