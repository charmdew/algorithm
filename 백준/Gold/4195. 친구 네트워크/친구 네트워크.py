import sys

input = sys.stdin.readline


def union(a, b):
    p_a = find(a)
    p_b = find(b)
    
    if p_a == p_b:
        return

    if p_a != p_b:
        parent[p_b] = p_a
        cnt[p_a] += cnt[p_b]


def find(x):
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]


for _ in range(int(input())):
    F = int(input())

    # 부모를 자기 자신으로 초기화
    parent = [i for i in range(2*F)]

    # 친구 네트워크에 몇 명 있는지 저장
    cnt = [1]*2*F

    # 친구 인덱스 저장
    f_idx = dict()
    idx = 0

    for i in range(F):
        f1, f2 = input().rstrip().split()

        if f1 not in f_idx:
            f_idx[f1] = idx
            idx += 1
        if f2 not in f_idx:
            f_idx[f2] = idx
            idx += 1

        # 친구 네트워크 형성
        union(f_idx[f1], f_idx[f2])

        # 친구 네트워크에 몇 명 있는지 출력
        print(cnt[parent[f_idx[f1]]])