n = int(input())

arr =[0 for _ in range(1000001)]
arr[1]=1
for i in range(2, n+1):
    arr[i] = arr[i-2]+arr[i-1]
    if arr[i] >= 1000000007:
        arr[i] = arr[i] % 1000000007
    #print(arr[i],arr[i-2],arr[i-1])
print(arr[n])