n = int(input())
arr=[i for i in range(1,n+1)]
arr2 =[]
c =0
while True:
    if len(arr) == 1:
        break
    arr2.append(arr.pop(c))
    a = arr.pop(c)
    arr.append(a)
for i in range(len(arr2)):
    print(arr2[i], end=" ")
    
print(arr[0])