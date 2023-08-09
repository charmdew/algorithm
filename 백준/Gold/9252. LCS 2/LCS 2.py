"""
[풀이]
LCS[i][j] : A의 i번째까지 문자열과 B의 j번째까지의 문자열의 LCS 값을 의미함

A[i] == B[j] 인 경우
    LCS[i][j] = LCS[i-1][j-1] + A[i]
A[i] != B[j] 인 경우 
    LCS[i-1][j]와 LCS[i][j-1]의 길이를 비교하여 길이가 더 긴 값으로 대입
"""

import sys

input = sys.stdin.readline

A = [""] + list(input().rstrip())
B = [""] + list(input().rstrip())

LA, LB = len(A), len(B)
LCS = [[""]*LB for _ in range(LA)]

for i in range(1, LA):
    for j in range(1, LB):
        if A[i] == B[j]:
            LCS[i][j] = LCS[i-1][j-1] + A[i]
        else:
            if len(LCS[i-1][j]) > len(LCS[i][j-1]):
                LCS[i][j] = LCS[i-1][j]
            else:
                LCS[i][j] = LCS[i][j-1]

answer = LCS[-1][-1]
print(len(answer))
print(answer)