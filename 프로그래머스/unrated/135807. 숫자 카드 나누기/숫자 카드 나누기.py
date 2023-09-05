result = 0

def gcd(a, b):
    global result 
    
    if b == 0:
        result = a
        return
    
    gcd(b, a%b)

def solution(arrayA, arrayB):
    global result 
    
    answer = 0
    
    # 중복된 원소 제거
    arrayA = list(set(arrayA))
    arrayB = list(set(arrayB))
    
    # 정렬
    arrayA.sort()
    arrayB.sort()
        
    # arrayA의 최대 공약수 구하기
    gcdA = arrayA[0]
    for i in range(1, len(arrayA)):
        gcd(gcdA, arrayA[i])
        gcdA = result
        
    # arrayA의 최대공약수로 arrayB의 원소를 나눌 수 있는지 확인
    # 하나라도 나눌 수 있다면 안됨
    div = False
    for b in arrayB:
        if b % gcdA == 0:
            div = True
            break
    if not div:
        answer = gcdA
    
    # arrayB의 최대 공약수 구하기
    gcdB = arrayB[0]
    for i in range(1, len(arrayB)):
        gcd(gcdB, arrayB[i])
        gcdB = result
        
    # arrayB의 최대공약수로 arrayA의 원소를 나눌 수 있는지 확인
    # 하나라도 나눌 수 있다면 안됨
    div = False
    for a in arrayA:
        if a % gcdB == 0:
            div = True
            break
    if not div:
        answer = max(answer, gcdB)
    
    return answer