n=int(input())
last = 0 # 짝수면 sk차례

while True:
    if n ==1:
        break
    if n <3:
        n -=1
        last+=1
    elif n ==3:
        n-=2
        last+=2
    else:
        n-=3
        last +=1

if last %2 ==0:
    print("SK")
else:
    print("CY")