import sys

input = sys.stdin.readline

N, M = map(int, input().split())
tree = list(map(int, input().split()))

s, e = 0, max(tree)

result = 0

while s <= e:
    h = (s + e)//2

    # 자른 나무의 길이
    cut = 0
    for t in tree:
        if h < t:
            cut += (t-h)

    # 만약 자른 나무의 길이가 M 이상이라면 길이 늘리기
    if cut >= M:
        result = h
        s = h + 1
    # 만약 자른 나무의 길이가 M보다 작다면 길이 줄이기
    else:
        e = h - 1

print(result)