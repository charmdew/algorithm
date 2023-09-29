# number에서 k개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자

from itertools import combinations

def solution(number, k):
    answer = ''
    
    stack = []
    for num in number:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
        
    answer = "".join(stack)
            
    return answer