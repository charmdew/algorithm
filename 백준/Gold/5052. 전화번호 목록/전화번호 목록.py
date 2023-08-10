"""
다른사람 풀이
- 실행 시간 더 짧음!
"""

from sys import stdin
input=stdin.readline
n=int(input())
for i in range(n):
    m=int(input())
    L=[]
    for j in range(m):
        L.append(input().rstrip())
    L.sort()
    fin=False
    for j in range(m-1):
        if L[j]==L[j+1][:len(L[j])]:
            fin=True
            break
    if fin:
        print("NO")
    else:
        print("YES")