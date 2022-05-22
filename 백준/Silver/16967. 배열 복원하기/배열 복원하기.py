import sys

input = sys.stdin.readline

H, W, X, Y = map(int, input().split())

B = []
for _ in range(H+X):
    B.append(list(map(int, input().split())))

A = [[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        if i >= X and j >= Y:
            A[i][j] = B[i][j]-A[i-X][j-Y]
        else:
            A[i][j] = B[i][j]

for i in range(H):
    print(*A[i])