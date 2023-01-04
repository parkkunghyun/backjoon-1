from collections import deque
from collections import Counter
def solution(topping):
    answer = 0
    # 가짓수가동일해야함
    # 12131412 1213 1412
    t = Counter(topping)
    topping = deque(topping)
    
    setT = set()
    for i in range(len(topping)):
        p =topping.popleft()
        t[p] -=1
        setT.add(p)
        #print(p, t[p], setT)
        if t[p] ==0:
            t.pop(p)
        if len(t) == len(setT):
            answer +=1
    
    return answer