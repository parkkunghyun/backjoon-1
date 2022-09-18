n = int(input())

if n >=5:
    arr = []
    k = n //5
    for i in range(k+1):
        sum = 0
        div = n -(5*i)
        tt = div % 2
        
        if tt==0:
            sum =i+(div//2)
            arr.append(sum)
    print(min(arr))
            
else:
    t = n //2
    tt = n%2
    if tt !=0:
        print(-1)
    else:
        print(t)
    
