def solution(n, left, right):
    answer = []
    # 00 01 02 0 1 2
    # 10 11 12 3 4 5
    # 20 21 22 6 7 8
    
    for i in range(left, right+1):
        idiv = i //n
        imod = i % n
        if idiv>imod:
            answer.append(idiv+1)
        else:
            answer.append(imod+1)
    
    #print(answer)
    return answer