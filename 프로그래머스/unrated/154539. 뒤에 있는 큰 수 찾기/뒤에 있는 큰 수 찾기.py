# 스택 사용

def solution(numbers):
    N = len(numbers)
    
    answer = [-1]*N
    
    # 뒷 큰수를 찾아야할 후보들을 (인덱스, 원소값) 형태로 스택에 저장
    stack = []
    for i, n in enumerate(numbers):
        # 스택에 저장되어 있는 원소값보다 더 큰 수인 경우 뒷 큰수
        while stack and stack[-1][1] < n:
            idx, x = stack.pop()
            
            # 뒷 큰수 저장
            answer[idx] = n
            
        # 현재 원소값 스택에 저장
        stack.append((i, n))
            
    return answer