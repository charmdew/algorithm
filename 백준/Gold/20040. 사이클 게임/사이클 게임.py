import sys 

input = sys.stdin.readline

n, m = map(int, input().split())

parent = list(range(n))

def union(a, b):
    p_a = find(a)
    p_b = find(b)

    if p_a < p_b:
        parent[p_b] = p_a
    else:
        parent[p_a] = p_b

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])    
    return parent[x]

answer = 0
lines = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    a, b = lines[i]
    
    # 사이클이 완성되었는지 확인
    if(find(a) == find(b)):
        answer = i+1
        break

    # 두 점 연결
    union(a, b)

print(answer)