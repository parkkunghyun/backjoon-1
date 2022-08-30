import sys 

arr=[]

t = int(sys.stdin.readline().strip())
for i in range(t):
    n = sys.stdin.readline().split()
    if n[0] =='push':
        m = int(n[1])
        arr.append(m)
    elif n[0] == 'top':
        if arr:
            print(arr[len(arr)-1])
        else:
            print(-1)
    elif n[0]=='size':
        print(len(arr))
    elif n[0]=='empty':
        if arr:
            print(0)
        else:
            print(1)
    elif n[0] == 'pop':
        if arr:
            print(arr.pop())
        else:
            print(-1)