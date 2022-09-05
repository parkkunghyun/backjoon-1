n = int(input())

s = n
san = 0
while True:
    if s ==1:
        break 
    else:
        if s >3:
            s -= 3
            san +=1     
        else:
            s -=1
            san +=1
if san %2 ==0:
    print('CY')
else:
    print('SK')