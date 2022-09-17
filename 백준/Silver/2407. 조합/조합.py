n,m = map(int,input().split())

nmx=1
k = n-m+1
for i in range(k,n+1):
    nmx*=i
    
mx=1
for i in range(1,m+1):
    mx*=i 

result = nmx//mx
print(result)

