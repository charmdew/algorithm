import sys 
from collections import defaultdict

input = sys.stdin.readline 

N = int(input())

alphabet = defaultdict(int)

# 오른쪽에서 n번째 자리수일 때 알파벳에 10^(n-1) 만큼의 가중치 부여
for _ in range(N):
    word = input().rstrip()
    L = len(word)
    for i in range(L):
        alphabet[word[i]] += 10**(L-1-i)

# 내림차순 정렬
result = sorted(alphabet.items(), key=lambda x:-x[1])

# 수의 최대합 저장
max_sum = 0

# 순서대로 9부터 0까지 
num = 9
for x in result:
    max_sum += num*x[1]
    num -= 1

print(max_sum)