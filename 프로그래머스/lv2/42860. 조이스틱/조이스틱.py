def solution(name):
    answer = 0
    
    # 알파벳을 만들기 위한 최소 조작 횟수
    alphabet = {chr(ord('A')+i): (26-i if i>13 else i) for i in range(26)}
    # print(alphabet)
    
    # name의 길이
    N = len(name)

    # 양끝에서 연속으로 있는 A개수 비교하기
    l, r = 0, 0
    for i in range(N):
        if name[i]!='A':
            break
        l += 1
    for i in range(1, N+1):
        if name[-i]!='A':
            break
        r += 1
    print(l, r)
    
    return answer