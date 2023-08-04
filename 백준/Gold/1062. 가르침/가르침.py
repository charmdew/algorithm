# 일반적인 DFS는 시간초과 뜸. 비트마스킹 활용하기!!
import sys
from itertools import combinations

input = sys.stdin.readline


N, K = map(int, input().split())

# words : 각 단어를 '비트마스킹으로 상징'하여 저장
words = [0 for _ in range(N)]
for combi in range(N):
    tmp = input().rstrip()

    # word 배열에 각 문자의 비트마스킹 저장
    for ch in tmp:
        words[combi] = words[combi] | (1 << (ord(ch) - ord('a')))

# edge cases
if K < 5:
    print(0)
    exit()
elif K == 26:
    print(N)
    exit()

# candi : 필수 글자를 제외한 알파벳
# need : 필수 알파벳
candi = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']
need = ['a', 'c', 't', 'i', 'n']
mxv = 0
for combi in combinations(candi, K - 5):
    learn = 0
    cnt = 0

    # need + combi 단어를 학습
    for ch in need:
        learn = learn | (1 << (ord(ch) - ord('a')))
    for ch in combi:
        learn = learn | (1 << (ord(ch) - ord('a')))

    # word가 learn에 완전히 커버되는지
    for word in words:
        if word & learn == word:
            cnt += 1
    mxv = max(mxv, cnt)
print(mxv)