arr =[0 for i in range(101)]

arr[1] = 1
arr[2] = 1
for i in range(3,len(arr)):
    arr[i] = arr[i-2] + arr[i-3]
n=int(input())
for i in range(n):
    k = int(input())
    print(arr[k])
    