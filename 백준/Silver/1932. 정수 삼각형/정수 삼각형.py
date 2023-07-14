import sys

input = sys.stdin.readline 

# 삼각형의 크기 n(1 ≤ n ≤ 500) 입력
n = int(input())

triangle = [list(map(int, input().split())) for _ in range(n)]

# DP 활용
# triangle[i][j] = max(triangle[i-1][j-1], triangle[i-1][j]) + triangle[i][j]
for i in range(1, n):
    for j in range(i+1):
        # 가장 왼쪽
        if j==0:
            triangle[i][j] += triangle[i-1][j]
        # 가장 오른쪽
        elif j==i:
            triangle[i][j] += triangle[i-1][j-1]
        # 중간
        else:
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])

# 맨 아래층에서 최댓값 구하기
print(max(triangle[n-1]))