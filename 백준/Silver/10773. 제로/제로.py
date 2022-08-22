import sys  
k = int(sys.stdin.readline())

sum =0
arr=[]
for _  in range(k):
    m = int(sys.stdin.readline())
    if m ==0:
        if not arr:
            continue 
        else:
            arr.pop()
    else:
        arr.append(m)
for i in arr:
    sum += i 
print(sum)
    