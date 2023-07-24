"""
https://school.programmers.co.kr/questions/12126

[유클리드 호제법 사용]
두 수 a,b가 있을 때 (a>b)
a%b==0 이면 b가 GCD임
a%b!=0 이면 (c=a%b라고 할 때)
b%c를 구해서 0이 나올때까지 반복함
"""

# 두수의 최대공약수 저장
gcd = 0

# 최대공약수 구하기
def GCD(a, b): 
    global gcd 
    
    if a % b == 0:
        gcd = b
        return
    else:        
        GCD(b, a%b)

# 최소공배수 구하기
def LCM(a, b):
    global gcd
    
    GCD(max(a, b), min(a, b))
    
    return a*b//gcd


def solution(arr):    
        
    # 세수 a, b, c의 최소공배수
    # = 두 수 a, b의 최소공배수인 l과 c의 최소공배수 lcm
    while len(arr)> 1:
        a = arr.pop()
        b = arr.pop()
        
        arr.append(LCM(a, b))
        
    answer = arr[0]
    
    return answer