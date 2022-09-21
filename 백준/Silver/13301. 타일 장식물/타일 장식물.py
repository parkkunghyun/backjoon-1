n =int(input())

arr =[0,1]

for i in range(1,n+2):
    arr.append(arr[i-1]+arr[i])
    
sum= arr[n] *2 + arr[n+1]*2
print(sum)