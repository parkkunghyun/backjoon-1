from collections import deque
def solution(order):
    answer = 0
    q = [i for i in range(1,len(order)+1)]
    q = deque(q)
    stack = deque()
    orderCount = 0
    while q:
        if order[orderCount] != q[0]:
            if stack and order[orderCount] == stack[-1]:
                orderCount +=1
                stack.pop()
            else:
                stack.append(q.popleft())
        else:
            orderCount+=1
            q.popleft()
            
    while stack:
        if order[orderCount] == stack[-1]:
            orderCount+=1
            stack.pop()
        else:
            break
        
    return orderCount