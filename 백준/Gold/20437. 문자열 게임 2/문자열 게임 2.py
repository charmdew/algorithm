import sys

input = sys.stdin.readline

for _ in range(int(input())):
    W = input().rstrip()
    K = int(input())

    # 문자열 W의 길이
    N = len(W)

    # 문자 등장 횟수 저장
    cnt = {chr(ord('a')+i): 0 for i in range(26)}

    # 문자 등장 인덱스 저장
    idx = {chr(ord('a')+i): [] for i in range(26)}

    # 3번을 만족하는 연속 문자열의 길이
    s, e = -1, -1
    # 4번을 만족하는 연속 문자열의 길이
    s4, e4 = -1, -1

    for i in range(N):
        x = W[i]

        cnt[x] += 1
        idx[x].append(i)

        # K개 이상이라면
        if cnt[x] >= K:
            if s == -1 or i-idx[x][-K] < e-s:
                s, e = idx[x][-K], i

            if s4 == -1 or i-idx[x][-K] > e4-s4:
                s4, e4 = idx[x][-K], i

    # print("3번", s, e)
    if s == -1:
        print(-1)
    else:
        print(e-s+1, e4-s4+1)
