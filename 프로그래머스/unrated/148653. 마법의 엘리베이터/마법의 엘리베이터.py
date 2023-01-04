def solution(storey):
    answer = 0
    # 5를기준으로나누기!
    while True:
        if storey==0:
            break
        s=storey % 10
        if s <5:
            answer +=s
        elif s >5:
            answer += 10 -s
            storey += 10- s
        else:
            if storey  //10 % 10 >=5:
                answer  += s
                storey +=  10-s
            else:
                answer +=s 
        storey = storey //10
    return answer