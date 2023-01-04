import itertools

def solution(k, dungeons):
    answer = 0
    d = itertools.permutations(dungeons,len(dungeons))
    
    for i in list(d):
        z = k
        #print(i)
        l =0
        for j in i:
            #print(j,"j")
            if z < j[0]:
                continue
            else:
                z -= j[1]
                l +=1
        #print(l,"ll")
        answer = max(answer,l)
    return answer