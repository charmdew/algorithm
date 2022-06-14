# 피보나치 수
n = int(input())

# 주기
p = 1500000

x1, x2 = 0, 1
for i in range(n%p-1):
    x1, x2 = x2, (x1+x2)%1000000

print(x2)