"""
[유클리드 호제법] 으로 최대 공약수 구하기
두 자연수 a, b에 대하여 a를 b로 나눈 나머지 r에 대해 
a와 b의 최대공약수는 b와 r의 최대공약수와 같다.
이를 계속 반복하며 b가 0이 될때, a값이 바로 최대공약수이다
"""
import sys
input = sys.stdin.readline


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def multiply(arr):
    return eval('*'.join([str(n) for n in arr]))


N = int(input())
A = multiply(list(map(int, input().split())))

M = int(input())
B = multiply(list(map(int, input().split())))


x = gcd(A, B)
print(str(x % 1000000000).zfill(9) if x >= 1000000000 else x)