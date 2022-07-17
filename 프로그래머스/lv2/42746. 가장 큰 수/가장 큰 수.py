def solution(numbers):
    answer = ''
    
    info = []
    for i, number in enumerate(numbers):
        x = str(number)
        info.append(((x*4)[0:4], i))
    info.sort(reverse=True)
    
    for inf in info:
        answer += str(numbers[inf[1]])
        
    answer = str(int(answer))
    
    return answer